from src._botDiscord import BotDiscord
import os
from dotenv import load_dotenv
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



    bot.run(os.getenv("discord_token"))