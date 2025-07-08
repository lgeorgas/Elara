import asyncio
from config import set_main_loop

def register_bot_events(bot):
    @bot.event
    async def on_ready():
        set_main_loop(asyncio.get_running_loop())
        print(f"✅ Bot is ready. Captured event loop.")