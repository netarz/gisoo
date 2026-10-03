#!/usr/bin/env bash
# Point Claude Code at Gisoo for this shell session, then start it.
#   source claude-code/env.sh && claude
# Note: the base URL has no /v1 at the end; Claude Code adds /v1/messages itself.
export ANTHROPIC_BASE_URL="https://gisoo.pro/api"
export ANTHROPIC_AUTH_TOKEN="${GISOO_API_KEY:?set GISOO_API_KEY to your sk-gisoo-v1-... key first}"
export ANTHROPIC_MODEL="claude-sonnet-5-5"
export ANTHROPIC_DEFAULT_HAIKU_MODEL="claude-haiku-4-5"
