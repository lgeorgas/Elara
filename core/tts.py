from config import client_eleven, ELEVENLABS_VOICE_ID
from io import BytesIO
import asyncio

async def synthesize_tts(user_id, text):
    try:
        audio_stream = await asyncio.to_thread(
            lambda: client_eleven.text_to_speech.convert(
                text=text,
                voice_id=ELEVENLABS_VOICE_ID,
                model_id="eleven_multilingual_v2"
            )
        )
        buffer = BytesIO(b"".join(audio_stream))
        buffer.seek(0)
        return buffer
    except Exception as e:
        print(f"❌ [{user_id}] TTS failed: {e}")
        return None