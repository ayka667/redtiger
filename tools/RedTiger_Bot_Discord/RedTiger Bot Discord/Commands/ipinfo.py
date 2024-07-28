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
    import subprocess

    class Command(commands.Cog):
        def __init__(self, bot):
            self.bot = bot

        @commands.command(aliases=['ipgeo', 'geoip'])
        async def ipinfo(self, ctx, *, ip: str = None):
            command_logs("ipinfo")

            if ip is None:
                await ctx.send(f"{ctx.author.mention}: **Invalid IP.** \nExample: 1.1.1.1")
                return
            
            try:
                try:
                    if sys.platform.startswith("win"):
                        result = subprocess.run(['ping', '-n', '1', ip], capture_output=True, text=True, timeout=1)
                    elif sys.platform.startswith("linux"):
                        result = subprocess.run(['ping', '-c', '1', '-W', '1', ip], capture_output=True, text=True, timeout=1)
                    if result.returncode == 0:
                        ping = "Succeed"
                    else:
                        ping = "Fail"
                except:
                    ping = "Fail"

                try:
                    response = requests.get(f"https://{website}/api/ip/ip={ip}")
                    api = response.json()

                    ip = api['ip']
                    status = api['status']
                    country = api['country']
                    country_code = api['country_code']
                    region = api['region']
                    region_code = api['region_code']
                    zip = api['zip']
                    city = api['city']
                    latitude = api['latitude']
                    longitude = api['longitude']
                    timezone = api['timezone']
                    isp = api['isp']
                    org = api['org']
                    as_host = api['as']
                    loc_url = api['loc_url']

                except:
                    response = requests.get(f"http://ip-api.com/json/{ip}")
                    api = response.json()

                    try:
                        if api['status'] == "success": status = "Valid"
                        else: status = "Invalid"
                    except: 
                        status = "Invalid"

                    try: country = api['country']
                    except: country = "None"
                    try: country_code = api['countryCode']
                    except: country_code = "None"
                    try: region = api['regionName']
                    except: region = "None"
                    try: region_code = api['region']
                    except: region_code = "None"
                    try: zip = api['zip']
                    except: zip = "None"
                    try: city = api['city']
                    except: city = "None"
                    try: latitude = api['lat']
                    except: latitude = "None"
                    try: longitude = api['lon']
                    except: longitude = "None"
                    try: timezone = api['timezone']
                    except: timezone = "None"
                    try: isp = api['isp']
                    except: isp = "None"
                    try: org = api['org']
                    except: org = "None"
                    try: as_host = api['as']
                    except: as_host = "None"
                    loc_url = f"https://www.google.com/maps/search/?api=1&query={latitude},{longitude}"


                embed = discord.Embed(
                    title=f"Info: \"{ip}\":", 
                    color=discord.Color(int(f"0x{EMBED_COLOR}", 16)),
                    timestamp=datetime.datetime.utcnow()
                )
                embed.add_field(name="****Ip:****", value=f"```{ip}```", inline=True)
                embed.add_field(name="****Ping:****", value=f"```{ping}```", inline=True)
                embed.add_field(name="****Status:****", value=f"```{status}```", inline=True)
                embed.add_field(name="****Country:****", value=f"```{country} ({country_code})```", inline=True)
                embed.add_field(name="****Region:****", value=f"```{region} ({region_code})```", inline=True)
                embed.add_field(name="****Zip:****", value=f"```{zip}```", inline=True)
                embed.add_field(name="****City:****", value=f"```{city}```", inline=True)
                embed.add_field(name="****Latitude:****", value=f"```{latitude}```", inline=True)
                embed.add_field(name="****Longitude:****", value=f"```{longitude}```", inline=True)
                embed.add_field(name="****Timezone:****", value=f"```{timezone}```", inline=True)
                embed.add_field(name="****Isp:****", value=f"```{isp}```", inline=True)
                embed.add_field(name="****Org:****", value=f"```{org}```", inline=True)
                embed.add_field(name="****As:****", value=f"```{as_host}```", inline=True)
                embed.add_field(name="****Position:****", value=f"{loc_url}", inline=True)
                embed.set_footer(text="RedTiger")
                await ctx.send(embed=embed)
            except Exception as e:
                error_message(e)

    def setup(bot):
        bot.add_cog(Command(bot))

except Exception as e:
    error_logs(e)
