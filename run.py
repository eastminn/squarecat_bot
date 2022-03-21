#run.py
import discord, asyncio, datetime, pytz

client = discord.Client()

@client.event
async def on_ready():
    print("고먐미 봇이 실행됩니다.")
    await client.change_presence(status=discord.Status.online, activity=discord.Game("instagram : @dev.eastmin")) # 봇의 상태메세지를 설정한다.

@client.event
async def on_message(message):
    # 특정한 명령어에 대한 반응
    if message.content == "!인사": # '!인사'를 입력한다면
        await message.channel.send ("{} | {}님 안녕하세요!".format(message.author, message.author.mention)) # 작성된 채널에 메세지 출력
        await message.author.send ("{} | {}님 안녕하세요!".format(message.author, message.author.mention)) # 작성한 유저에게 DM으로 메세지 출력

    # 가독성을 위한 임베드 출력
    if message.content == "!정보": # '!정보'를 입력한다면
        embed = discord.Embed(title="고먐미", description="프로젝트용으로 개발중인 봇",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x4c2896)
        embed.add_field(name="다양한 기능들 추가 예정", value="시간날 떄마다 추가할 예정입니다.", inline=False)
        embed.add_field(name="GitHub", value="https://github.com/eastminn", inline=False)
        embed.set_footer(text="Bot Made by 김동민#0026, 문의는 DM으로 부탁드립니다 💬", icon_url="https://cdn.discordapp.com/attachments/955360993729449987/955392163158569021/IMG_20220320_042000_013.jpg")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/955360993729449987/955392404280737812/99pk9saw36t7q8t3o0gt.jpg")
    
        await message.channel.send(embed=embed) # 메세지를 채팅방에 출력한다.

    # 권한을 통해 메세지 삭제 기능
    if message.content.startswith ("!청소"): # '!청소'를 입력한다면
        if message.author.guild_permissions.administrator: # 입력한 유저의 권한을 확인한다.
            amount = message.content[4:] # '!청소 숫자' 에서 숫자를 인식하여 amount의 값을 넣는다.
            await message.delete()
            await message.channel.purge(limit=int(amount))
            embed = discord.Embed(title="🧹 청소 기능", description="{} 개의 메세지가 삭제되었습니다.".format(amount),timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x4c2896 )
            embed.add_field(name="청소한 사람", value=f"{message.author} ( {message.author.mention} )", inline=False)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/955360993729449987/955519503159160842/201503181440069692_img_0.gif")
            

            await message.channel.send(embed=embed)

        else: # 입력한 유저가 권한이 없다면,
            await message.delete() # 입력한 채팅을 삭제하고, 
            await message.channel.send("{}, 당신은 명령어를 사용할 수 있는 권한이 없습니다".format(message.author.mention)) # 문장을 출력한다.
            
    # 인증 기능
    if message.content.startswith ("!인증"): # '!인증'을 입력한다면
        if message.author.guild_permissions.administrator: # 입력한 유저의 권한을 확인한다.
            await message.delete() # 입력한 채팅을 삭제한다.
            user = message.mentions[0] # '!인증 @유저' 에서 유저정보를 user에 담는다.

            # 가독성을 위한 임베드 출력
            embed = discord.Embed(title="👋 인증 시스템", description="인증이 정상적으로 완료 되었습니다 !",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x4c2896)
            embed.add_field(name="인증 대상자", value=f"{user.name} ( {user.mention} )", inline=False)
            embed.add_field(name="담당 관리자", value=f"{message.author} ( {message.author.mention} )", inline=False)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/955360993729449987/955392404280737812/99pk9saw36t7q8t3o0gt.jpg")
            embed.set_footer(text="Bot Made by 김동민#0026, , 문의는 DM으로 부탁드립니다 💬", icon_url="https://cdn.discordapp.com/attachments/955360993729449987/955392163158569021/IMG_20220320_042000_013.jpg")
            await message.author.send (embed=embed) # 유저 개인 DM으로 전송한다. 채팅방에 출력되도록 하려면 messae.channel.send 로 바꾸면 된다.
            role = discord.utils.get(message.guild.roles, name = '유저 😀')
            await user.add_roles(role)

        else: # 권한이 없다면
            await message.delete() # 입력한 메세지를 삭제하고,
            await message.channel.send(embed=discord.Embed(title="권한 부족", description = message.author.mention + "님은 권한이 없습니다", color = 0x4c2896)) # 특정 문구를 출력한다.
            embed.set_footer(text="Bot Made by 김동민#0026, , 문의는 DM으로 부탁드립니다 💬", icon_url="https://cdn.discordapp.com/attachments/955360993729449987/955392163158569021/IMG_20220320_042000_013.jpg")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/955360993729449987/955392404280737812/99pk9saw36t7q8t3o0gt.jpg")


# 봇을 실행시키기 위해서 봇의 토큰을 작성하는 곳
client.run("자신이 생성한 봇의 토큰")
