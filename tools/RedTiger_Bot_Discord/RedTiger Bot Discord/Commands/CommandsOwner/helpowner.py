# Copyright (c) RedTiger (https://redtiger.online/)
# ----------------------------------------------------------------------------------------------------------------------------------------------------------|
# EN: - Do not touch or modify the code below. If there is an error, please contact the owner, but under no circumstances should you touch the code.
#     - Please do not share the code and keep it for yourself.
#
# FR: - Ne pas toucher ni modifier le code ci-dessous. En cas d'erreur, veuillez contacter le propriétaire, mais en aucun cas vous ne devez toucher au code.
#     - Merci de ne pas partager le code et de le garder pour vous.
from Commands.Config.Config import *
from Commands.Config.Util import *

try:
    import discord
    from discord.ext import commands
    import datetime

    intents = discord.Intents.default()
    intents.messages = True
    intents.guilds = True

    bot = commands.Bot(command_prefix=PREFIX, intents=intents, help_command=None)

    class Command(commands.Cog):
        def __init__(self, bot):
            self.bot = bot

        @commands.command()
        async def helpowner(self, ctx):
            if ctx.author.id != CREATOR_ID:
                await ctx.send("**You are not authorized to use this command.**")
                return
            
            command_logs("helpowner")
            try:
                    embed = discord.Embed(
                        title = "Help Owner", 
                        color = discord.Color(int(f"0x{EMBED_COLOR}", 16)),
                        timestamp = datetime.datetime.utcnow()
                    )
                    embed.add_field(name=f"{PREFIX}sendmpmessage `[message]`", value=f"Allows you to send a pm message to all server users.", inline=False)
                    embed.add_field(name=f'{PREFIX}sendembed `DESCRIPTION=="""[description]""" TITLE=="""[title]"""`', value=f"Allows you to send an embed in the channel.", inline=False)
                    embed.set_footer(text="RedTiger")
                    await ctx.send(embed=embed)
            except Exception as e:
                    await ctx.send(error_message(e))

    def setup(bot):
        bot.add_cog(Command(bot))
except Exception as e:
    error_logs(e)