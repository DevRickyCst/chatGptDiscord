import os

from dotenv import load_dotenv

from cogs.src._botDiscord import BotDiscord
from cogs.src._chatGpt import Gpt
from cogs.src._googleTTS import GoogleTTS as gTTS

load_dotenv()

cogs = ["openai", "textToSpeech"]


async def load_env():
    for cog in cogs:
        try:
            await bot.load_extension(cog)
        except:
            f"Couldn't load {cog} module"


if __name__ == "__main__":

    bot = BotDiscord()
    gpt = Gpt(os.getenv("openai_api_key"))

    @bot.event
    async def on_ready():
        print(f"Connecté en tant que {bot.user.name} ({bot.user.id})")
        print("------")

        await load_env()

    bot.run(os.getenv("discord_token"))
