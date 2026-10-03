"""Chat with any Gisoo model through the official OpenAI SDK.

Run:
    pip install -r requirements.txt
    export GISOO_API_KEY="sk-gisoo-v1-..."
    python chat.py

Docs: https://gisoo.pro/docs/chat
"""
import os

from openai import OpenAI

client = OpenAI(
    base_url=os.getenv("GISOO_BASE_URL", "https://gisoo.pro/api/v1"),
    api_key=os.environ["GISOO_API_KEY"],
)

# Any id from https://gisoo.pro/models works here, e.g.
# "openrouter/anthropic/claude-sonnet-4.5", "gemini-3.1-pro-preview", "deepseek-v4-flash".
MODEL = os.getenv("GISOO_MODEL", "gpt-4o-mini")

response = client.chat.completions.create(
    model=MODEL,
    messages=[
        {"role": "system", "content": "شما دستیار فارسی‌زبان هستید. کوتاه و دقیق جواب بدهید."},
        {"role": "user", "content": "برای یک نانوایی محلی یک شعار کوتاه بنویسید."},
    ],
    # Always send max_tokens: credit for the largest possible answer is reserved
    # before the call, so a cap keeps that reservation small.
    max_tokens=200,
)

print(response.choices[0].message.content)
print(f"\nrequest id: {response.id} | tokens: {response.usage.total_tokens}")
