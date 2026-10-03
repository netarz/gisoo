"""Make a short video through Gisoo: create a job, poll it, download the MP4.

Run:
    pip install -r requirements.txt
    export GISOO_API_KEY="sk-gisoo-v1-..."
    python video.py

A failed render is refunded automatically (status "failed", refunded: true).
Docs: https://gisoo.pro/docs/video
"""
import os
import time

import requests

BASE = "https://gisoo.pro/api/v1"
HEADERS = {"Authorization": f"Bearer {os.environ['GISOO_API_KEY']}"}

job = requests.post(
    f"{BASE}/videos",
    headers=HEADERS,
    json={
        "model": os.getenv("GISOO_VIDEO_MODEL", "sora-2"),  # or "veo-3.1-lite", "veo-3.1-fast"
        "prompt": "Slow aerial shot over a misty tea plantation in northern Iran at dawn, soft light",
        "seconds": "8",
        "size": "1280x720",
    },
    timeout=60,
).json()

# Ask every 10-20 seconds; a render takes from one to several minutes.
while job.get("status") in ("queued", "in_progress"):
    time.sleep(15)
    job = requests.get(f"{BASE}/videos/{job['id']}", headers=HEADERS, timeout=30).json()
    print(job["status"], job.get("progress"))

if job.get("status") == "completed":
    with requests.get(f"{BASE}/videos/{job['id']}/content", headers=HEADERS, stream=True, timeout=300) as r:
        r.raise_for_status()
        with open("video.mp4", "wb") as f:
            for chunk in r.iter_content(1 << 16):
                f.write(chunk)
    print("saved video.mp4")
else:
    print("not made:", job)
