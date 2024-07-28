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
    import base64

    class Command(commands.Cog):
        def __init__(self, bot):
            self.bot = bot

        @commands.command(aliases=['lookup'])
        async def userinfo(self, ctx, *, user_id: str = None):
            command_logs("userinfo")
            
            if user_id is None:
                await ctx.send(f"{ctx.author.mention}: **Invalid ID.** \nExample: 11223344556677889900")
                return
            if not user_id.isdigit():
                await ctx.send(f"{ctx.author.mention}: **Invalid ID.** \nExample: 11223344556677889900")
                return
            
            encodedBytes = base64.b64encode(user_id.encode("utf-8"))
            OnePartToken = str(encodedBytes, "utf-8")
            motifs = ["=", "==", "==="]
            for motif in motifs:
                if OnePartToken.endswith(motif):
                    OnePartToken = OnePartToken[:-2]

            user_id = int(user_id)
            
            try:
                user = await self.bot.fetch_user(user_id)
                member = ctx.guild.get_member(user_id)

                if isinstance(member, discord.Member):
                    nickname = member.nick
                else:
                    nickname = "None"

                embed_previous_names = ""
                async for message in ctx.channel.history(limit=100):
                    if message.author.id == user.id:
                        previous_name = message.author.display_name
                        if previous_name not in embed_previous_names:
                            embed_previous_names += f"{previous_name}\n"

                embed = discord.Embed(
                    title=f"Info \"{user.name}\":", 
                    color=discord.Color(int(f"0x{EMBED_COLOR}", 16)),
                    timestamp=datetime.datetime.utcnow()
                )
                
                embed.set_thumbnail(url=user.avatar_url)
                embed.add_field(name="****Username:****", value=f"```{user.name}```", inline=True)
                embed.add_field(name="****Discriminator:****", value=f"```{user.discriminator}```", inline=True)
                embed.add_field(name="****Display Name:****", value=f"```{user.display_name}```", inline=True)
                embed.add_field(name="****Mention:****", value=f"<@{user.id}>", inline=True)
                embed.add_field(name="****Nickname:****", value=f"```{nickname}```", inline=True)
                embed.add_field(name="****Id:****", value=f"```{user.id}```", inline=True)
                embed.add_field(name="****Bot:****", value=f"```{user.bot}```", inline=True)
                embed.add_field(name="****Prevname:****", value=f"```{embed_previous_names or 'None'}```", inline=True)
                embed.add_field(name="****Created At:****", value=f"```{user.created_at.strftime('%Y/%m/%d %H:%M:%S')}```", inline=True)
                embed.add_field(name="****One Part Token:****", value=f"```{OnePartToken}.```", inline=True)
                embed.add_field(name="****Avatar Url:****", value=f"{user.avatar_url}", inline=True)
                embed.set_footer(text="RedTiger")
                await ctx.send(embed=embed)
            
            except discord.NotFound:
                await ctx.send(f"{ctx.author.mention}: **User cannot be found.**")
            except discord.HTTPException as e:
                await ctx.send(error_message(e))
            except discord.Forbidden:
                await ctx.send("**I don't have permission to fetch this user.**")
            except Exception as e:
                await ctx.send(error_message(e))

    def setup(bot):
        bot.add_cog(Command(bot))
except Exception as e:
    error_logs(e)