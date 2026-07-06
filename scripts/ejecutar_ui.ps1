$ErrorActionPreference = "Stop"

$projectRoot = Split-Path -Parent $PSScriptRoot
$localVenv = Join-Path $projectRoot ".venv\Scripts\python.exe"
$parentVenv = Join-Path (Split-Path -Parent $projectRoot) ".venv\Scripts\python.exe"

if (Test-Path $localVenv) {
    $python = $localVenv
} elseif (Test-Path $parentVenv) {
    $python = $parentVenv
} else {
    Write-Host "No encontre un entorno virtual. Ejecuta: python -m venv .venv"
    exit 1
}

Set-Location $projectRoot
& $python -m pytest -m ui
