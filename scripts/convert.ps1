# Konvertiert alle Markdown-Dateien im output-Ordner zu Word-Dokumenten
# Ausführen: .\convert.ps1

param(
    [string]$InputPath = "output",
    [switch]$KeepMarkdown = $false
)

Write-Host "=== Markdown -> Word Konvertierung ===" -ForegroundColor Cyan
Write-Host ""

# Prüfen ob Pandoc installiert ist
if (!(Get-Command pandoc -ErrorAction SilentlyContinue)) {
    Write-Host "FEHLER: Pandoc ist nicht installiert!" -ForegroundColor Red
    Write-Host "Bitte zuerst .\setup.ps1 ausführen." -ForegroundColor Yellow
    exit 1
}

# Alle .md Dateien im Output-Ordner finden
$mdFiles = Get-ChildItem -Path $InputPath -Filter "*.md" -ErrorAction SilentlyContinue

if ($mdFiles.Count -eq 0) {
    Write-Host "Keine Markdown-Dateien in '$InputPath' gefunden." -ForegroundColor Yellow
    exit 0
}

Write-Host "Gefundene Dateien: $($mdFiles.Count)" -ForegroundColor Gray
Write-Host ""

foreach ($file in $mdFiles) {
    $outputFile = $file.FullName -replace '\.md$', '.docx'
    $outputName = Split-Path $outputFile -Leaf

    Write-Host "Konvertiere: $($file.Name) -> $outputName" -ForegroundColor Yellow

    # Pandoc Konvertierung mit besserer Formatierung
    pandoc $file.FullName `
        -o $outputFile `
        --from markdown `
        --to docx `
        --reference-doc=$null `
        2>&1 | Out-Null

    if (Test-Path $outputFile) {
        Write-Host "  -> Erfolgreich!" -ForegroundColor Green

        if (!$KeepMarkdown) {
            # Optional: Markdown-Datei behalten oder löschen
            # Remove-Item $file.FullName
        }
    } else {
        Write-Host "  -> FEHLER bei Konvertierung!" -ForegroundColor Red
    }
}

Write-Host ""
Write-Host "=== Konvertierung abgeschlossen ===" -ForegroundColor Cyan
Write-Host "Word-Dateien befinden sich in: $InputPath" -ForegroundColor White
