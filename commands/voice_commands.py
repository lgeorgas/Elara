from discord.ext import commands, voice_recv
from discord import FFmpegPCMAudio
import io
from config import client_eleven, ELEVENLABS_VOICE_ID, client_openai
from core.playback import play_audio
from core.audio_handler import build_audio_handler

def register_voice_commands(bot):
    @bot.command()
    async def summon(ctx):
        if ctx.author.voice is None:
            await ctx.send("You are not connected to a voice channel.")
            return
        channel = ctx.author.voice.channel
        if ctx.voice_client:
            if ctx.voice_client.channel == channel:
                await ctx.send(f"I'm already in {channel.name}")
                return
            await ctx.send(f"Leaving {ctx.voice_client.channel.name} for {channel.name}")
            await ctx.voice_client.disconnect()
        vc = await channel.connect(cls=voice_recv.VoiceRecvClient)
        sink = voice_recv.BasicSink(build_audio_handler(ctx))
        vc.listen(sink)
        await ctx.send(f"Joined {channel} and am listening!")

    @bot.command()
    async def leave(ctx):
        if ctx.voice_client:
            await ctx.voice_client.disconnect()
            await ctx.send("Disconnected from voice.")
        else:
            await ctx.send("Not in a voice channel.")

    @bot.command()
    async def say(ctx, *, text):
        await ctx.send(f"Speaking: {text}")
        audio_stream = client_eleven.text_to_speech.convert(
            voice_id=ELEVENLABS_VOICE_ID,
            model_id="eleven_multilingual_v2",
            text=text
        )
        buffer = io.BytesIO(b"".join(audio_stream))
        buffer.seek(0)
        await play_audio(ctx, buffer)

    @bot.command()
    async def ask(ctx, *, prompt):
        await ctx.send("Thinking...")
        system_prompt = {
            "role": "system",
            "content": open("prompts/elara_system_prompt.txt").read()
        }
        user_prompt = {"role": "user", "content": prompt}
        try:
            response = client_openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[system_prompt, user_prompt],
                temperature=0.8
            )
            reply = response.choices[0].message.content.strip()
            await ctx.send(f"Elara says: {reply}")
            audio_stream = client_eleven.text_to_speech.convert(
                voice_id=ELEVENLABS_VOICE_ID,
                model_id="eleven_multilingual_v2",
                text=reply
            )
            buffer = io.BytesIO(b"".join(audio_stream))
            buffer.seek(0)
            await play_audio(ctx, buffer)
        except Exception as e:
            await ctx.send(f"An error occurred: {e}")