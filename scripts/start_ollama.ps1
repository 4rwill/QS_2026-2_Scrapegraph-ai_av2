$ErrorActionPreference = 'Stop'
$taskRoot = Split-Path $PSScriptRoot -Parent
$ollamaRoot = Join-Path $taskRoot '.tools/ollama'
$env:OLLAMA_MODELS = Join-Path $ollamaRoot 'models'
$env:OLLAMA_HOST = '127.0.0.1:11434'
New-Item -ItemType Directory -Force $env:OLLAMA_MODELS | Out-Null
$server = Start-Process -FilePath (Join-Path $ollamaRoot 'ollama.exe') -ArgumentList 'serve' -WindowStyle Hidden -PassThru -RedirectStandardOutput (Join-Path $ollamaRoot 'server-out.log') -RedirectStandardError (Join-Path $ollamaRoot 'server-err.log')
$server.Id | Set-Content (Join-Path $ollamaRoot 'server.pid')
Write-Output "Ollama PID $($server.Id), endpoint $env:OLLAMA_HOST, models $env:OLLAMA_MODELS"
