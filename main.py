from discord.ext import commands
from config import bot, DISCORD_TOKEN
from core.bot_events import register_bot_events
from commands.voice_commands import register_voice_commands

# Register event hooks
register_bot_events(bot)

# Register commands
register_voice_commands(bot)

if __name__ == "__main__":
    bot.run(DISCORD_TOKEN)