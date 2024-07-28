# Copyright (c) RedTiger (https://redtiger.online/)
# ----------------------------------------------------------------------------------------------------------------------------------------------------------|
# EN: - Do not touch or modify the code below. If there is an error, please contact the owner, but under no circumstances should you touch the code.
#     - Please do not share the code and keep it for yourself.
#
# FR: - Ne pas toucher ni modifier le code ci-dessous. En cas d'erreur, veuillez contacter le propriétaire, mais en aucun cas vous ne devez toucher au code.
#     - Merci de ne pas partager le code et de le garder pour vous.

from Commands.Config.Config import *

import colorama
import discord
import datetime
from discord.ext import commands
import sys
import os

color = colorama.Fore
red = color.RED
white = color.WHITE
reset = color.RESET
command = f"{red}[{white}>{red}] |"
info = f"{red}[{white}!{red}] |"
error = f"{red}[{white}x{red}] |"

def command_logs(command_name):
    print(f"{red}{command} Command: {white}{command_name}{red}{reset}")

def error_logs(e):
    print(f"{red}{error} Error: {white}{e}{red}{reset}")

def error_message(e):
    message = f"""# Error:
```{e}```"""
    return message

def Clear():
    if sys.platform.startswith("win"):
        "WINDOWS"
        os.system("cls")
    elif sys.platform.startswith("linux"):
        "LINUX"
        os.system("clear")