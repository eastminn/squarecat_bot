#run.py
import discord, asyncio, datetime, pytz, os
from discord.ext import commands
import os

client = commands.Bot(command_prefix="!") # 접두사를 설정해준다.

for filename in os.listdir("basics"):
    if filename.endswith(".py"):
        client.load_extension(f"basics.{filename[:-3]}")

for filename in os.listdir("crawling"):
    if filename.endswith(".py"):
        client.load_extension(f"crawling.{filename[:-3]}")

@client.event
async def on_ready():
    print("고먐미 봇이 실행됩니다.")
    await client.change_presence(status=discord.Status.online, activity=discord.Game("고먐미 봇은 " + str(len(client.guilds)) + "개의 서버에 접속하고 있어요!")) # 봇의 상태메세지를 설정한다.

# 봇을 실행시키기 위해서 봇의 토큰을 작성하는 곳
client.run("ODAyNTI3NzAwNTY4MjQ0MjI0.YAwiKg.Aup_sI3vO2T8DOyTIk_xBtj49kI")
