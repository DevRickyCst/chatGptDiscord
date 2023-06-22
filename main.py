from src._botDiscord import BotDiscord
import os
from dotenv import load_dotenv
from src._googleTTS import GoogleTTS as gTTS
from src._chatGpt import Gpt

load_dotenv()
if __name__ =='__main__':

    bot = BotDiscord()
    gpt = Gpt(os.getenv("openai_api_key"))


    @bot.command()
    async def chat_gpt(ctx, *args):
        texte = ' '.join(args)
        response = gpt.call_chat(texte)
        await bot.send_message(ctx, response ,False)

    @bot.command()
    async def img_gpt(ctx, *args):
        texte = ' '.join(args)
        response = gpt.call_image(texte)
        await bot.send_message(ctx, response ,False)
    
    @bot.command()
    async def trad_gpt(ctx, *args):
        lang = args[0]
        texte = ' '.join(args[1:])
        response = gpt.call_traduction(lang,texte)
        await bot.send_message(ctx, response ,False)

    @bot.command()
    async def parle(ctx, *args):
        channel = ctx.author.voice.channel if ctx.author.voice!=None else None
        message = ' '.join(args) if len(args)>=1 else 'SMAB'
        if channel!=None and ctx.voice_client==None:
            await bot.play_audio(gTTS.get_audio_fp(message), channel)

    bot.run(os.getenv("discord_token"))