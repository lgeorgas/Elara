import os
import tempfile
from discord import FFmpegPCMAudio

async def play_audio(ctx, buffer):
    if not ctx.voice_client or not ctx.voice_client.is_connected():
        print("❌ Voice client not available.")
        return

    if ctx.voice_client.is_playing():
        print("⏸ Already playing audio.")
        return

    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmpfile:
        buffer.seek(0)
        tmpfile.write(buffer.read())
        tmpfile.flush()
        path = tmpfile.name

    def after_playing(error):
        if error:
            print(f"❌ Playback error: {error}")
        try:
            os.remove(path)
            print(f"🧹 Deleted temp file: {path}")
        except Exception as e:
            print(f"❌ Could not delete temp file: {e}")

    try:
        source = FFmpegPCMAudio(path)
        ctx.voice_client.play(source, after=after_playing)
        print(f"▶️ Playing {path}")
    except Exception as e:
        print(f"❌ Failed to play audio: {e}")