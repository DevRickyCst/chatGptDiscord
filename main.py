from src.bot import BotDiscord
import os
from dotenv import load_dotenv

load_dotenv()
if __name__ =='__main__':

    bot = BotDiscord()


    @bot.command()
    async def chat_gpt(ctx, *args):
        texte = ' '.join(args)
        await bot.send_message(ctx, texte ,False)

    bot.run(os.getenv("discord_token"))