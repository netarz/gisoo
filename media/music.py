"""Make a music clip through Gisoo (Lyria) and save it as MP3.

Run:
    pip install -r requirements.txt
    export GISOO_API_KEY="sk-gisoo-v1-..."
    python music.py

For a full song with lyrics use "openrouter/google/lyria-3-pro-preview" and put the
lyrics in the prompt. Docs: https://gisoo.pro/docs/music
"""
import base64
import os

import requests

res = requests.post(
    "https://gisoo.pro/api/v1/audio/music",
    headers={"Authorization": f"Bearer {os.environ['GISOO_API_KEY']}"},
    json={
        "model": "openrouter/google/lyria-3-clip-preview",
        "prompt": "Calm podcast background with setar and soft percussion, slow tempo, no vocals",
    },
    timeout=120,
)
res.raise_for_status()
track = res.json()

with open("music.mp3", "wb") as f:
    f.write(base64.b64decode(track["data"][0]["b64_json"]))
print("saved music.mp3", track.get("text"))
