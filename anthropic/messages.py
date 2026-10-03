"""Claude through Gisoo with the official Anthropic SDK (Messages API).

Run:
    pip install -r requirements.txt
    export GISOO_API_KEY="sk-gisoo-v1-..."
    python messages.py

The Messages API is served on gisoo.pro only, not on netarz.ir/api/ai/v1.
Docs: https://gisoo.pro/docs/anthropic
"""
import os

import anthropic

client = anthropic.Anthropic(
    base_url="https://gisoo.pro/api",  # not .../v1: the SDK adds /v1/messages itself
    api_key=os.environ["GISOO_API_KEY"],
)

message = client.messages.create(
    model="claude-sonnet-5-5",
    max_tokens=400,
    system="کوتاه و دقیق، به فارسی جواب بده.",
    messages=[{"role": "user", "content": "فرق git merge و git rebase را در سه خط بگو."}],
)

print(message.content[0].text)
print(f"\nid: {message.id} | input: {message.usage.input_tokens} | output: {message.usage.output_tokens}")
