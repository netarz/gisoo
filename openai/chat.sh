#!/usr/bin/env bash
# Chat completion on Gisoo with plain curl, plus the public model list (no key needed).
#   GISOO_API_KEY="sk-gisoo-v1-..." ./chat.sh
set -euo pipefail

BASE="${GISOO_BASE_URL:-https://gisoo.pro/api/v1}"

# 1. No key needed: the chat models and their prices
curl -sS "${BASE}/models?type=chat" | head -c 600
echo

# 2. A chat completion
curl -sS "${BASE}/chat/completions" \
  -H "Authorization: Bearer ${GISOO_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-4o-mini",
    "max_tokens": 200,
    "messages": [{"role": "user", "content": "سلام! یک جملهٔ انگیزشی کوتاه بنویس."}]
  }'
echo

# 3. Your balance and this key's limits
curl -sS "${BASE}/me" -H "Authorization: Bearer ${GISOO_API_KEY}"
echo
