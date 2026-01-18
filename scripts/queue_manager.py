#!/usr/bin/env python3
"""
Queue Manager for Worker System
Handles job picking, completion, and status tracking.

Commands:
  pick [--worker ID]    - Pick next available job
  done <filename>       - Mark job as completed
  status                - Show queue status
  recover-zombies       - Reset orphaned IN_PROGRESS jobs
  retry_git <cmd>       - Execute git command with retry
"""

import os
import sys
import json
import time
import random
import subprocess
import re
import socket
from datetime import datetime
from pathlib import Path

# Force UTF-8 output on Windows
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

QUEUE_DIR = Path("tickets/queue")


def generate_worker_id():
    """Generate a short, readable worker ID (2 letters + 2 digits)."""
    import string
    letters = ''.join(random.choices(string.ascii_uppercase, k=2))
    digits = ''.join(random.choices(string.digits, k=2))
    return f"W-{letters}{digits}"


def extract_worker_id_from_filename(filename: str) -> str:
    """Extract worker ID from filename."""
    # Format: job27_W3_IN_PROGRESS.json or job27_W3_DONE.json
    match = re.search(r'_([^_]+)_(IN_PROGRESS|DONE)\.json$', filename)
    if match:
        return match.group(1)
    return None


def pick_job(worker_id: str = None):
    """
    Pick an available job from the queue.
    Returns JSON content on stdout, or status messages.
    """
    if not worker_id:
        worker_id = generate_worker_id()

    if not QUEUE_DIR.exists():
        print("QUEUE_EMPTY")
        return

    all_jobs = list(QUEUE_DIR.glob("*.json"))

    if not all_jobs:
        print("QUEUE_EMPTY")
        return

    # Categorize jobs
    in_progress = [j for j in all_jobs if "_IN_PROGRESS" in j.stem]
    pending = [j for j in all_jobs if "_IN_PROGRESS" not in j.stem and "_DONE" not in j.stem]

    # Separate finalizer jobs
    finalizer_jobs = [j for j in pending if j.stem.startswith("job_z_")]
    regular_pending = [j for j in pending if not j.stem.startswith("job_z_")]

    def claim_job(chosen: Path) -> dict:
        """Claim a job: rename file, update JSON with worker info."""
        with open(chosen, 'r', encoding='utf-8') as f:
            job_data = json.load(f)

        job_data['worker_id'] = worker_id
        job_data['picked_at'] = datetime.now().isoformat()
        job_data['picked_by_hostname'] = socket.gethostname()

        new_name = chosen.parent / f"{chosen.stem}_{worker_id}_IN_PROGRESS.json"

        with open(new_name, 'w', encoding='utf-8') as f:
            json.dump(job_data, f, indent=2, ensure_ascii=False)

        chosen.unlink()
        return job_data

    # Pick regular jobs first
    if regular_pending:
        regular_pending.sort(key=lambda x: x.name)

        for chosen in regular_pending:
            try:
                job_data = claim_job(chosen)
                print(json.dumps(job_data, indent=2, ensure_ascii=False))
                return
            except (FileNotFoundError, OSError, json.JSONDecodeError):
                continue

    # Handle finalizer
    if finalizer_jobs:
        chosen = finalizer_jobs[0]

        finalizer_in_progress = [j for j in in_progress if j.stem.startswith("job_z_")]
        if finalizer_in_progress:
            print("NO_MORE_JOBS")
            return

        try:
            job_data = claim_job(chosen)
        except (FileNotFoundError, OSError):
            print("NO_MORE_JOBS")
            return

        other_in_progress = [j for j in in_progress if not j.stem.startswith("job_z_")]
        if other_in_progress:
            job_data["_wait_for_others"] = True
            job_data["_other_in_progress_count"] = len(other_in_progress)

        print(json.dumps(job_data, indent=2, ensure_ascii=False))
        return

    # No pending jobs
    if in_progress:
        finalizer_in_progress = [j for j in in_progress if j.stem.startswith("job_z_")]
        if len(finalizer_in_progress) == len(in_progress):
            print("NO_MORE_JOBS")
        else:
            print("WAITING_FOR_OTHERS")
    else:
        print("QUEUE_EMPTY")


def mark_done(job_filename: str):
    """Mark a job as done by renaming from _IN_PROGRESS to _DONE."""
    stem = job_filename.replace(".json", "")

    # Parse filename: job27_W3_IN_PROGRESS
    match = re.match(r'^(.+)_([^_]+)_IN_PROGRESS$', stem)
    if match:
        base_name = match.group(1)
        worker_id = match.group(2)
    else:
        base_name = stem.replace("_IN_PROGRESS", "")
        worker_id = None

    # Find the in-progress file
    in_progress_file = None

    if worker_id:
        candidate = QUEUE_DIR / f"{base_name}_{worker_id}_IN_PROGRESS.json"
        if candidate.exists():
            in_progress_file = candidate

    if not in_progress_file:
        for f in QUEUE_DIR.glob(f"{base_name}*_IN_PROGRESS*.json"):
            in_progress_file = f
            if not worker_id:
                worker_id = extract_worker_id_from_filename(f.name)
            break

    if not in_progress_file:
        exact = QUEUE_DIR / job_filename
        if exact.exists():
            in_progress_file = exact

    if in_progress_file and in_progress_file.exists():
        if worker_id:
            done_name = f"{base_name}_{worker_id}_DONE.json"
        else:
            done_name = f"{base_name}_DONE.json"
        done_file = QUEUE_DIR / done_name
        in_progress_file.rename(done_file)
        print(f"Marked as done: {done_file.name}")
    else:
        print(f"Error: Could not find in-progress job for {job_filename}", file=sys.stderr)
        sys.exit(1)


def recover_zombies():
    """Find all IN_PROGRESS jobs and mark them for zombie recovery."""
    if not QUEUE_DIR.exists():
        print("Queue directory does not exist")
        return

    in_progress = list(QUEUE_DIR.glob("*_IN_PROGRESS*.json"))

    if not in_progress:
        print("No zombie jobs found")
        return

    print(f"Found {len(in_progress)} potential zombie jobs:")

    recovered = 0
    for job_file in in_progress:
        with open(job_file, 'r', encoding='utf-8') as f:
            job_data = json.load(f)

        original_worker = job_data.get('worker_id', 'unknown')
        original_picked = job_data.get('picked_at', 'unknown')

        job_data['zombie_recovery'] = True
        job_data['zombie_original_worker'] = original_worker
        job_data['zombie_original_picked_at'] = original_picked
        job_data['zombie_recovered_at'] = datetime.now().isoformat()

        job_data.pop('worker_id', None)
        job_data.pop('picked_at', None)
        job_data.pop('picked_by_hostname', None)

        # Extract base name
        original_stem = job_file.stem
        match = re.match(r'^(.+)_[^_]+_IN_PROGRESS$', original_stem)
        if match:
            base_stem = match.group(1)
        else:
            base_stem = original_stem.replace("_IN_PROGRESS", "")

        new_filename = f"{base_stem}.json"
        new_path = QUEUE_DIR / new_filename

        with open(new_path, 'w', encoding='utf-8') as f:
            json.dump(job_data, f, indent=2, ensure_ascii=False)

        job_file.unlink()

        print(f"  [OK] Recovered: {job_file.name}")
        print(f"       Original worker: {original_worker}, picked: {original_picked}")
        recovered += 1

    print(f"\nRecovered {recovered} zombie jobs")


def retry_git(command: str, max_retries: int = 5):
    """Execute a git command with retry logic for lock file issues."""
    for attempt in range(max_retries):
        try:
            result = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True,
                timeout=60
            )

            if result.returncode == 0:
                print(result.stdout)
                return

            if "lock" in result.stderr.lower() or "index.lock" in result.stderr:
                wait_time = random.uniform(1, 3)
                print(f"Git lock detected, waiting {wait_time:.1f}s (attempt {attempt + 1}/{max_retries})")
                time.sleep(wait_time)
                continue
            else:
                print(f"Git error: {result.stderr}", file=sys.stderr)
                sys.exit(1)

        except subprocess.TimeoutExpired:
            print(f"Git command timed out (attempt {attempt + 1}/{max_retries})")
            time.sleep(2)
            continue

    print(f"Git command failed after {max_retries} attempts", file=sys.stderr)
    sys.exit(1)


def show_status():
    """Show current queue status."""
    if not QUEUE_DIR.exists():
        print("Queue directory does not exist")
        return

    all_jobs = list(QUEUE_DIR.glob("*.json"))

    pending = [j for j in all_jobs if "_IN_PROGRESS" not in j.stem and "_DONE" not in j.stem]
    in_progress = [j for j in all_jobs if "_IN_PROGRESS" in j.stem]
    done = [j for j in all_jobs if "_DONE" in j.stem]

    # Count zombies
    zombie_count = 0
    for j in pending:
        try:
            with open(j, 'r', encoding='utf-8') as f:
                data = json.load(f)
                if data.get('zombie_recovery'):
                    zombie_count += 1
        except:
            pass

    print(f"Queue Status:")
    print(f"  Pending: {len(pending)}" + (f" ({zombie_count} zombies)" if zombie_count else ""))
    print(f"  In Progress: {len(in_progress)}")
    print(f"  Done: {len(done)}")

    if pending:
        print(f"\nPending jobs:")
        for j in sorted(pending, key=lambda x: x.name)[:10]:
            print(f"  - {j.name}")
        if len(pending) > 10:
            print(f"  ... and {len(pending) - 10} more")

    if in_progress:
        print(f"\nCurrently processing:")
        for j in in_progress:
            worker_id = extract_worker_id_from_filename(j.name)
            if worker_id:
                print(f"  - {j.name} (Worker: {worker_id})")
            else:
                print(f"  - {j.name}")


def main():
    if len(sys.argv) < 2:
        print("Usage: queue_manager.py <command> [args]")
        print("")
        print("Commands:")
        print("  pick [--worker ID]    - Pick next job")
        print("  done <filename>       - Mark job as completed")
        print("  status                - Show queue status")
        print("  recover-zombies       - Reset orphaned IN_PROGRESS jobs")
        print("  retry_git <cmd>       - Execute git command with retry")
        print("")
        print("Examples:")
        print("  python scripts/queue_manager.py pick")
        print("  python scripts/queue_manager.py pick --worker W3")
        print("  python scripts/queue_manager.py status")
        sys.exit(1)

    command = sys.argv[1]

    if command == "pick":
        worker_id = None
        if "--worker" in sys.argv:
            worker_idx = sys.argv.index("--worker")
            if worker_idx + 1 < len(sys.argv):
                worker_id = sys.argv[worker_idx + 1]
        pick_job(worker_id)
    elif command == "done":
        if len(sys.argv) < 3:
            print("Error: Missing filename argument", file=sys.stderr)
            sys.exit(1)
        mark_done(sys.argv[2])
    elif command == "recover-zombies":
        recover_zombies()
    elif command == "retry_git":
        if len(sys.argv) < 3:
            print("Error: Missing git command argument", file=sys.stderr)
            sys.exit(1)
        git_cmd = " ".join(sys.argv[2:])
        retry_git(git_cmd)
    elif command == "status":
        show_status()
    else:
        print(f"Unknown command: {command}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
