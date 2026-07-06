$projectRoot = Split-Path -Parent $PSScriptRoot
$report = Join-Path $projectRoot "reports\report.html"

if (Test-Path $report) {
    Start-Process $report
} else {
    Write-Host "Todavia no existe reports\report.html. Ejecuta primero las pruebas."
}
