
Elara Discord Bot - Refactored Structure & Documentation
#########################################################

This project implements "Elara Nytheris", a persona-driven Discord bot with hotword detection, STT (Whisper),
LLM (OpenAI), and TTS (ElevenLabs) capabilities. This document explains the modular file structure and the purpose
of each module after the July 2025 refactor.

------------------------------------
Folder Structure
------------------------------------

Elara/
├── main.py
├── config.py
├── prompts/
│   └── elara_system_prompt.txt
├── core/
│   ├── audio_handler.py
│   ├── hotword_detector.py
│   ├── llm.py
│   ├── tts.py
│   ├── playback.py
│   └── bot_events.py
├── commands/
│   └── voice_commands.py
├── utils/
|    └── audio_utils.py

------------------------------------
File Descriptions
------------------------------------

main.py
---
- Entry point of the bot.
- Loads the bot object from config.py.
- Registers events and commands from bot_events.py and voice_commands.py.
- Starts the bot using the DISCORD_TOKEN.

config.py
-----
- Centralized configuration.
- Loads environment variables (.env) such as API keys.
- Instantiates the Discord bot object and sets its command prefix and intents.
- Initializes ElevenLabs and OpenAI API clients.
- Defines global constants for audio buffering and bot state.
- Provides shared global variables: `audio_buffers`, `last_check_time`, `main_loop`.

prompts/elara_system_prompt.txt
---------------
- Stores the persistent persona definition of Elara for OpenAI prompts.

commands/voice_commands.py
--------------
- Defines voice-related commands:
  - !summon: Join user's voice channel and start listening.
  - !leave: Disconnect from voice.
  - !say <text>: TTS Elara's voice via ElevenLabs.
  - !ask <question>: Get an OpenAI response and read it aloud.

core/bot_events.py
----------
- Registers lifecycle events (e.g. on_ready).
- Captures and stores the asyncio event loop for cross-thread scheduling.

core/audio_handler.py
---------
- `on_audio(ctx, user_id, data)`: Called for each audio packet from a user.
- Buffers PCM audio in a fixed-length deque per user.
- Checks cooldown and passes large enough buffers to Whisper.
- `build_audio_handler(ctx)`: Wraps `on_audio` to include context.
- `audio_buffers` is a defaultdict of deques (one per user).

core/hotword_detector.py
------------
- Saves user audio buffer to WAV.
- Submits audio to Whisper via OpenAI API.
- Searches for the hotword (e.g. "Elara").
- If detected, triggers LLM response + TTS playback.

core/llm.py
-------
- Sends prompt to OpenAI using `gpt-3.5-turbo`.
- Loads system prompt from `prompts/elara_system_prompt.txt`.
- Returns Elara's response text.

core/tts.py
-------
- Synthesizes text-to-speech using ElevenLabs API.
- Returns a BytesIO audio buffer suitable for playback.

core/playback.py
--------
- Plays audio to the Discord voice channel using FFmpeg.
- Writes temp WAV files and auto-deletes after playback.
- Handles Discord voice client availability and error checking.

core/audio_utils.py
-----------
- Saves raw PCM frames to a .wav file using `wave` module.
- Used before sending to Whisper for STT.

------------------------------------
Execution Flow (Hotword Flow)
------------------------------------

1. User joins voice channel and issues `!summon`.
2. Bot connects using `VoiceRecvClient` and starts `BasicSink(build_audio_handler(ctx))`.
3. As audio packets are received, `on_audio` buffers them.
4. If buffer size and cooldown allow, a hotword check is triggered.
5. If Whisper detects "Elara", the remaining message is sent to OpenAI.
6. OpenAI generates a reply, which is sent to ElevenLabs.
7. The audio is streamed back to the user in the voice channel.

------------------------------------
Dependencies
------------------------------------

- discord.py with voice_recv extension
- OpenAI Python SDK
- elevenlabs Python SDK
- ffmpeg (must be in system PATH)
- python-dotenv

------------------------------------
Maintainer Notes
------------------------------------

- Ensure your `.env` contains:
  DISCORD_TOKEN#...
  ELEVEN_API_KEY#...
  OPENAI_API_KEY#...

- `main_loop` is automatically captured on bot startup and used for async execution from non-async code.
- Modular design allows plug-and-play changes to LLM, TTS, hotword logic, and persona scripting.

