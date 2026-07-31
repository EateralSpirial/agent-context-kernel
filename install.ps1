$ErrorActionPreference = "Stop"
$Installer = Join-Path $PSScriptRoot "scripts/install.py"

$Python = Get-Command python -ErrorAction SilentlyContinue
if ($Python) {
    & $Python.Source $Installer @args
    exit $LASTEXITCODE
}

$PyLauncher = Get-Command py -ErrorAction SilentlyContinue
if ($PyLauncher) {
    & $PyLauncher.Source -3 $Installer @args
    exit $LASTEXITCODE
}

throw "Python 3 is required"
