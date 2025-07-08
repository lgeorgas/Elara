import time
from collections import defaultdict, deque
from config import MAX_FRAMES, audio_buffers, last_check_time, get_main_loop
from core.hotword_detector import check_for_hotword

def build_audio_handler(ctx):
    def wrapped_on_audio(user, data):
        user_id = user.id
        on_audio(ctx, user_id, data)
    return wrapped_on_audio

# def initialize_audio_buffers():
#     global audio_buffers
#     audio_buffers = defaultdict(lambda: deque(maxlen=MAX_FRAMES))

def on_audio(ctx, user_id, data):
    if user_id not in audio_buffers:
        print(f"🔊 Starting new buffer for {user_id}")

    audio_buffers[user_id].append(data.pcm)

    now = time.time()
    cooldown = 10

    if len(audio_buffers[user_id]) >= MAX_FRAMES:
        if user_id not in last_check_time or now - last_check_time[user_id] > cooldown:
            last_check_time[user_id] = now
            frames_copy = audio_buffers[user_id].copy()
            audio_buffers[user_id].clear()

            def on_done(fut):
                try:
                    print(f"✅ Hotword check finished: {fut.result()}")
                except Exception as e:
                    print(f"❌ Hotword check failed: {e}")

            try:
                loop = get_main_loop()
                future = loop.run_in_executor(None, check_for_hotword, ctx, user_id, frames_copy)
                future.add_done_callback(on_done)
            except Exception as e:
                print(f"❌ Could not submit hotword task: {e}")
        else:
            print(f"⏳ Cooldown active for {user_id}")