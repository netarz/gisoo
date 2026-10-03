"""Text to speech and speech to text through Gisoo.

Run:
    pip install -r requirements.txt
    export GISOO_API_KEY="sk-gisoo-v1-..."
    python speech.py

Docs: https://gisoo.pro/docs/audio
"""
import os

from openai import OpenAI

client = OpenAI(base_url="https://gisoo.pro/api/v1", api_key=os.environ["GISOO_API_KEY"])

# 1. Text to speech: a short Persian ad read aloud.
#    "gemini-3.8-flash-tts" has 30 voices and takes tone directions.
speech = client.audio.speech.create(
    model="gpt-4o-mini-tts",
    voice="nova",
    input="نان تازهٔ سنگک، هر روز از ساعت شش صبح. منتظرتان هستیم.",
    response_format="mp3",
)
speech.write_to_file("ad.mp3")
print("saved ad.mp3")

# 2. Speech to text: turn the same file back into text.
#    "gemini-3.5-transcribe" can also label speakers (response_format="diarized_json") or return SRT.
with open("ad.mp3", "rb") as audio:
    text = client.audio.transcriptions.create(model="gpt-4o-mini-transcribe", file=audio)
print(text.text)
