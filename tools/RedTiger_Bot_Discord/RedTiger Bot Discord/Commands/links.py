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

    class Command(commands.Cog):
        def __init__(self, bot):
            self.bot = bot

        @commands.command(aliases=['invite', 'link', 'add', 'discord', 'server', 'github', 'website', 'site', 'tool', 'addme', 'telegram', 'canal'])
        async def links(self, ctx):
            command_logs("links")
            try:
                    embed = discord.Embed(
                        title = "Links",
                        description = f"""
- <:links_logo_red:1193987708113141830> [Discord Server](https://{discord_server})
- <:website_logo_red:1188140372879216801> [Website](https://{website})
- <:telegram_logo_red:1227740512824332310> [Telegram](https://{telegram})
- <:github_logo_red:1188139048393506837> [Tool Github](https://{github_tool})""",
                        color = discord.Color(int(f"0x{EMBED_COLOR}", 16)),
                        timestamp = datetime.datetime.utcnow()
                    )
                    embed.set_footer(text="RedTiger")
                    await ctx.send(embed=embed)
            except Exception as e:
                    await ctx.send(error_message(e))

    def setup(bot):
        bot.add_cog(Command(bot))
except Exception as e:
    error_logs(e)