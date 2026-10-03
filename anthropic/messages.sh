#!/usr/bin/env bash
# The Anthropic Messages API on Gisoo with plain curl.
#   GISOO_API_KEY="sk-gisoo-v1-..." ./messages.sh
set -euo pipefail

curl -sS https://gisoo.pro/api/v1/messages \
  -H "Authorization: Bearer ${GISOO_API_KEY}" \
  -H "anthropic-version: 2023-06-01" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "claude-haiku-4-5",
    "max_tokens": 200,
    "messages": [{"role": "user", "content": "سلام! خودت را در یک جمله معرفی کن."}]
  }'
echo
