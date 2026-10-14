param([Parameter(ValueFromRemainingArguments=$true)][string[]]$AssistantArgs)
$projectRoot = Split-Path -Parent $PSScriptRoot
$env:PYTHONPATH = Join-Path $projectRoot 'src'
python -m assistente.cli @AssistantArgs
exit $LASTEXITCODE
