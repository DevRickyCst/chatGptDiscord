from discord.ext import commands
from cogs.src._googleTTS import GoogleTTS


class textToSpeech(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="parle")
    async def talk(self, ctx, *args):
        channel = ctx.author.voice.channel if ctx.author.voice != None else None
        message = " ".join(args) if len(args) >= 1 else "SMAB"
        if channel != None and ctx.voice_client == None:
            await self.bot.play_audio(GoogleTTS.get_audio_fp(message), channel)
