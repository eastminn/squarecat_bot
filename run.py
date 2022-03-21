#run.py
import discord, asyncio, datetime, pytz

client = discord.Client()

@client.event
async def on_ready():
    print("고먐미 봇이 실행됩니다.")
    await client.change_presence(status=discord.Status.online, activity=discord.Game("instagram : @dev.eastmin")) # 봇의 상태메세지를 설정한다.

@client.event
async def on_message(message):
    if message.content == "!인사": # '!인사'를 입력한다면
        await message.channel.send ("{} | {}님 안녕하세요!".format(message.author, message.author.mention)) # 작성된 채널에 메세지 출력
        await message.author.send ("{} | {}님 안녕하세요!".format(message.author, message.author.mention)) # 작성한 유저에게 DM으로 메세지 출력

    if message.content == "!정보": # '!정보'를 입력한다면
        embed = discord.Embed(title="고먐미", description="프로젝트용으로 개발중인 봇",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
        embed.add_field(name="다양한 기능들 추가 예정", value="시간날 떄마다 추가할 예정입니다.", inline=False)
        embed.set_footer(text="Bot Made by. 김동민#0026", icon_url="https://cdn.discordapp.com/attachments/955360993729449987/955392163158569021/IMG_20220320_042000_013.jpg")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/955360993729449987/955392404280737812/99pk9saw36t7q8t3o0gt.jpg")
    
        await message.channel.send(embed=embed) # 메세지를 채팅방에 출력한다.


# 봇을 실행시키기 위해서 봇의 토큰을 작성하는 곳
client.run("자신이 생성한 봇의 토큰")
