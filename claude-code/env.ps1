# Point Claude Code at Gisoo for this PowerShell session, then run `claude`.
#   . .\claude-code\env.ps1
# The base URL has no /v1 at the end; Claude Code adds /v1/messages itself.
if (-not $env:GISOO_API_KEY) { throw "Set GISOO_API_KEY to your sk-gisoo-v1-... key first." }
$env:ANTHROPIC_BASE_URL = "https://gisoo.pro/api"
$env:ANTHROPIC_AUTH_TOKEN = $env:GISOO_API_KEY
$env:ANTHROPIC_MODEL = "claude-sonnet-5-5"
$env:ANTHROPIC_DEFAULT_HAIKU_MODEL = "claude-haiku-4-5"
