# Copyright (c) RedTiger (https://redtiger.online/)
# ----------------------------------------------------------------------------------------------------------------------------------------------------------|
# EN: - Do not touch or modify the code below. If there is an error, please contact the owner, but under no circumstances should you touch the code.
#     - Please do not share the code and keep it for yourself.
#
# FR: - Ne pas toucher ni modifier le code ci-dessous. En cas d'erreur, veuillez contacter le propriétaire, mais en aucun cas vous ne devez toucher au code.
#     - Merci de ne pas partager le code et de le garder pour vous.

while True:
    try:
        try:
            from Commands.Config.Config import *
            from Commands.Config.Util import *

            import discord
            from discord.ext import commands
        except:
            import os
            os.system("pip3 install --upgrade pip")
            os.system("pip3 install discord.py==1.6.0")
            os.system("pip3 install datetime")
            os.system("pip3 install requests")
            os.system("pip3 install colorama")
            os.system("pip3 install phonenumbers")
            os.system("pip3 install time")

        intents = discord.Intents.default()

        intents.messages = True
        intents.guilds = True 
        intents.members = True

        bot = commands.Bot(command_prefix=PREFIX, intents=intents, help_command=None)
        @bot.event
        async def on_ready():
            Clear()
            await bot.change_presence(activity=discord.Game(name=f"Prefix: {PREFIX}"))
            print(f"""
{red}> Token    : {white}{TOKEN}{red}
{red}> Invite   : {white}https://discord.com/oauth2/authorize?client_id={bot.user.id}&scope=bot&permissions=8{red}
{red}> Username : {white}{bot.user.name}{red}
{red}> Tag      : {white}#{bot.user.discriminator}{red}
{red}> Id       : {white}{bot.user.id}{red}
{red}> Prefix   : {white}{PREFIX}{red}

{red}Logs:{reset}""")
            print(f'{color.RED}{info} Bot online.{color.RESET}')

        bot.load_extension("Commands.help")
        bot.load_extension("Commands.links")
        bot.load_extension("Commands.userinfo")
        bot.load_extension("Commands.ipinfo")
        bot.load_extension("Commands.numberinfo")
        bot.load_extension("Commands.cryptoprice")
        bot.load_extension("Commands.CommandsOwner.helpowner")
        bot.load_extension("Commands.CommandsOwner.sendmpmessage")
        bot.load_extension("Commands.CommandsOwner.ebookosintembed")
        bot.load_extension("Commands.CommandsOwner.sendembed")
        bot.run(TOKEN)

    except Exception as e:
        continue