from discord.ext import commands
from src._googleTTS import gTTS


class openai(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def parle(self, ctx, *args):
        channel = ctx.author.voice.channel if ctx.author.voice != None else None
        message = " ".join(args) if len(args) >= 1 else "SMAB"
        if channel != None and ctx.voice_client == None:
            await self.bot.play_audio(gTTS.get_audio_fp(message), channel)
