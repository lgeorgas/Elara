import os
from dotenv import load_dotenv
from discord.ext import commands
import discord
from elevenlabs import ElevenLabs
from openai import OpenAI
from collections import defaultdict, deque

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ELEVEN_API_KEY = os.getenv("ELEVEN_API_KEY")
ELEVENLABS_VOICE_ID = "tyQcMHLCDdilaVrZOlHc"

client_openai = OpenAI(api_key=OPENAI_API_KEY)
client_eleven = ElevenLabs(api_key=ELEVEN_API_KEY)

BUFFER_DURATION_SECONDS = 3
SAMPLE_RATE = 48000
CHANNELS = 2
SAMPLE_WIDTH = 2
CHUNK_SIZE = 960
MAX_FRAMES = (SAMPLE_RATE * BUFFER_DURATION_SECONDS) // CHUNK_SIZE

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

audio_buffers = defaultdict(lambda: deque(maxlen=MAX_FRAMES))  # will be initialized in audio_handler
last_check_time = {}  # global state for cooldown tracking

main_loop = None
def set_main_loop(loop):
    global main_loop
    main_loop = loop
def get_main_loop():
    return main_loop