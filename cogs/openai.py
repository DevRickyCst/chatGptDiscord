from discord.ext import commands

from cogs.src._chatGpt import Gpt


class openai(commands.Cog):
    def __init__(self, bot, api_key):
        self.bot = bot
        self.gpt = Gpt(api_key)

    @commands.command()
    async def chat_gpt(self, ctx, *args):
        texte = " ".join(args)
        response = self.gpt.call_chat(texte)
        await self.bot.send_message(ctx, response, False)

    @commands.command()
    async def img_gpt(self, ctx, *args):
        texte = " ".join(args)
        response = self.gpt.call_image(texte)
        await self.bot.send_message(ctx, response, False)

    @commands.command()
    async def trad_gpt(self, ctx, *args):
        lang = args[0]
        texte = " ".join(args[1:])
        response = self.gpt.call_traduction(lang, texte)
        await self.bot.send_message(ctx, response, False)
