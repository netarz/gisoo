"""Make an image through Gisoo (GPT Image or Nano Banana) and save it as PNG.

Run:
    pip install -r requirements.txt
    export GISOO_API_KEY="sk-gisoo-v1-..."
    python image.py

Image models: https://gisoo.pro/models?type=image  ·  Docs: https://gisoo.pro/docs/images
"""
import base64
import os

from openai import OpenAI

client = OpenAI(base_url="https://gisoo.pro/api/v1", api_key=os.environ["GISOO_API_KEY"])

result = client.images.generate(
    # "gemini-3.1-flash-image" is Nano Banana 2; "gpt-image-1.5" can return a transparent PNG.
    model=os.getenv("GISOO_IMAGE_MODEL", "gpt-image-1-mini"),
    prompt="Flat illustration of a Persian tea glass on a wooden table, warm morning light, no text",
    size="1024x1024",
    quality="medium",
)

with open("tea.png", "wb") as f:
    f.write(base64.b64decode(result.data[0].b64_json))
print("saved tea.png", result.usage)
