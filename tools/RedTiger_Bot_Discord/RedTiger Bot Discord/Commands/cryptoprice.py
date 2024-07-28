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
    import requests

    class Command(commands.Cog):
        def __init__(self, bot):
            self.bot = bot

        @commands.command()
        async def cryptoprice(self, ctx, *, symbol: str = None):
            command_logs("cryptoprice")

            if symbol is None:
                await ctx.send(f"{ctx.author.mention}: **Invalid Symbol.** \nExample: BTC/USDT")
                return

            try:
                if not symbol.islower():
                    if "/" in symbol:
                        crypto, _, money = symbol.partition('/')
                        symbol = crypto + money
                    else:
                        await ctx.send(f"{ctx.author.mention}: **Invalid Symbol.** \nExample: BTC/USDT")
                        return
                else:
                    await ctx.send(f"{ctx.author.mention}: **Invalid Symbol.** \nExample: BTC/USDT")
                    return

                api_url = "https://api.binance.com/api/v3/ticker/price"
                params = {"symbol": symbol}
                response = requests.get(api_url, params=params)
                if response.status_code == 200:
                    data = response.json()
                    cryptoprice = float(data["price"])

                    embed = discord.Embed(
                        title="Crypto Price", 
                        color=discord.Color(int(f"0x{EMBED_COLOR}", 16)),
                        description=f"""**Crypto:** {crypto}
**Money:** {money}
**{crypto} Price:** {'{:.8f}'.format(cryptoprice)} {money}""",
                        timestamp=datetime.datetime.utcnow()
                    )

                    embed.set_footer(text="RedTiger")
                    await ctx.send(embed=embed)
                else:
                    await ctx.send(f"{ctx.author.mention}: **Crypto cannot be found.**")
            except Exception as e:
                error_message(e)

    def setup(bot):
        bot.add_cog(Command(bot))
except Exception as e:
    error_logs(e)