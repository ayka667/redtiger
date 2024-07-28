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
        async def help(self, ctx):
            command_logs("help")
            try:
                    embed = discord.Embed(
                        title = "Help", 
                        color = discord.Color(int(f"0x{EMBED_COLOR}", 16)),
                        timestamp = datetime.datetime.utcnow()
                    )
                    embed.add_field(name=f"{PREFIX}links", value=f"Allows you to see all RedTiger links.", inline=False)
                    embed.add_field(name=f"{PREFIX}userinfo `[id]`", value=f"Allows you to retrieve information about a user.", inline=False)
                    embed.add_field(name=f"{PREFIX}ipinfo `[ip]`", value=f"Allows you to retrieve information from an IP.", inline=False)
                    embed.add_field(name=f"{PREFIX}numberinfo `[number]`", value=f"Allows you to retrieve information from a phone number.", inline=False)
                    embed.add_field(name=f"{PREFIX}cryptoprice `[CRYPTO]/[MONEY]`", value=f"Allows you to retrieve the price of a cryptocurrency.", inline=False)
                    embed.set_footer(text="RedTiger")
                    await ctx.send(embed=embed)
            except Exception as e:
                    await ctx.send(error_message(e))

    def setup(bot):
        bot.add_cog(Command(bot))

except Exception as e:
    error_logs(e)