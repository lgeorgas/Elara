import re
from utils.audio_utils import save_frames_to_wav
from config import client_openai, get_main_loop
from core.llm import query_llm
from core.tts import synthesize_tts
from core.playback import play_audio
import asyncio

def check_for_hotword(ctx, user_id, frames):
    print(f"🔍 Checking hotword for {user_id}")
    if not save_frames_to_wav(frames, "check.wav"):
        return

    try:
        with open("check.wav", "rb") as f:
            transcript = client_openai.audio.transcriptions.create(
                model="whisper-1",
                file=f
            )
    except Exception as e:
        print(f"❌ Whisper error: {e}")
        return

    text = transcript.text.strip().lower()
    print(f"🧠 [{user_id}] Transcript: {text}")

    match = re.search(r"\b[eai]?lara\b", text)
    if match:
        prompt = text[match.end():].lstrip(" ,").strip()
        print(f"✨ Hotword detected: '{prompt}'")
        asyncio.run_coroutine_threadsafe(respond_to_user(ctx, user_id, prompt), get_main_loop())
    else:
        print("🚫 No hotword detected")

async def respond_to_user(ctx, user_id, prompt):
    print(f"🤖 [{user_id}] Prompt: {prompt}")
    try:
        response = await query_llm(prompt)
        buffer = await synthesize_tts(user_id, response)
        if buffer:
            await play_audio(ctx, buffer)
    except Exception as e:
        print(f"❌ [{user_id}] Response error: {e}")