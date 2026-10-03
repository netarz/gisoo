"""Streaming (server-sent events) through Gisoo with the OpenAI SDK.

Run:
    export GISOO_API_KEY="sk-gisoo-v1-..."
    python stream.py
"""
import os

from openai import OpenAI

client = OpenAI(base_url="https://gisoo.pro/api/v1", api_key=os.environ["GISOO_API_KEY"])

stream = client.chat.completions.create(
    model=os.getenv("GISOO_MODEL", "gpt-4o-mini"),
    messages=[{"role": "user", "content": "یک متن کوتاه دربارهٔ چای لاهیجان بنویس."}],
    max_tokens=400,
    stream=True,
)
for chunk in stream:
    if chunk.choices and chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
print()
