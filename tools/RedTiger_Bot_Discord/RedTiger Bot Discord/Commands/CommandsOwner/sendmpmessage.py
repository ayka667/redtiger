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
    import time

    class Command(commands.Cog):
        def __init__(self, bot):
            self.bot = bot

        @commands.command()
        async def sendmpmessage(self, ctx, *, message: str):
            if ctx.author.id != CREATOR_ID:
                await ctx.send("**You are not authorized to use this command.**")
                return

            command_logs("sendmpmessage")
            sent_count = 0
            failed_count = 0
            guild = ctx.guild

            await guild.fetch_members(limit=None).flatten()

            for member in guild.members:
                if member != ctx.author:
                    try:
                        await member.send(message)
                        sent_count += 1
                        await ctx.send(f"Message sent to **{member.name}#{member.discriminator}** ({member.id})")
                        time.sleep(0.5)
                    except discord.Forbidden:
                        failed_count += 1
                        await ctx.send(f"Failed to send to **{member.name}#{member.discriminator}** ({member.id}): `Access denied.`")
                    except Exception as e:
                        failed_count += 1
                        await ctx.send(f"Error sending to **{member.name}#{member.discriminator}** ({member.id}): `{str(e)}`")

            total_members = len(guild.members) - 1

            await ctx.send(f"""Server: **{ctx.guild.name}**.
    Member(s): **{total_members}**.
    Message sent to: **{sent_count}** user(s). 
    Failed: **{failed_count}** user(s).""")

    def setup(bot):
        bot.add_cog(Command(bot))
except Exception as e:
    error_logs(e)