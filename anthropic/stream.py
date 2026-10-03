"""Streaming a Claude answer through Gisoo with the Anthropic SDK.

Run:
    export GISOO_API_KEY="sk-gisoo-v1-..."
    python stream.py
"""
import os

import anthropic

client = anthropic.Anthropic(base_url="https://gisoo.pro/api", api_key=os.environ["GISOO_API_KEY"])

with client.messages.stream(
    model="claude-haiku-4-5",
    max_tokens=600,
    messages=[{"role": "user", "content": "یک تابع پایتون بنویس که کد ملی ایران را اعتبارسنجی کند."}],
) as stream:
    for text in stream.text_stream:
        print(text, end="", flush=True)
print()
