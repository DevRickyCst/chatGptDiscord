import os
import discord
import asyncio
from discord.ext import commands

#Need it to start the bot
intents = discord.Intents.default()
intents.typing = False
intents.message_content = True

class BotDiscord(commands.Bot):

    def __init__(self, intents=intents, command_prefix='$') -> None:
        self.token = os.getenv("discord_token")
        commands.Bot.__init__(self, intents=intents,command_prefix='$')

    async def send_message(self, message, user_message, is_private):
        try:
            response = user_message
            print(response)
            await message.author.send(response) if is_private else await message.channel.send(response)
        except Exception as e:
            print(e)

    async def play_audio(self, ctx, audio):
        print('in play audio')
        FFMPEG_OPTIONS = {'options': '-vn'}
        try :
            await ctx.autor.voice.channel.connect()
            source = discord.FFmpegOpusAudio(audio, pipe=True, **FFMPEG_OPTIONS)
            voice_client = ctx.voice_client
            voice_client.play(source)
            while voice_client.is_playing():
                await asyncio.sleep(1)
            await voice_client.disconnect()

        except Exception as e:
            print(e)