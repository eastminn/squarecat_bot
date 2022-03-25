import discord, asyncio, datetime, pytz
from discord.ext import commands
from discord.utils import get
from discord import Member


client = commands.Bot(command_prefix='!')

class simple(commands.Cog): 

    def __init__(self, app):
        self.app = app 
    
    @commands.command(name="인사") # '!인사' 를 입력한다면
    async def hi(self, ctx): 
        await ctx.send("{} | {} 님 안녕하세요!".format(ctx.author, ctx.author.mention)) # 작성된 채널에 메세지를 출력한다.
        await ctx.author.send("{} | {} 님 안녕하세요!".format(ctx.author, ctx.author.mention)) # 작성한 유저에게 DM으로 메세지를 출력한다.

    @commands.command(name="정보") # '!정보'를 입력한다면
    async def information(self,ctx):
        embed = discord.Embed(title="고먐미", description="프로젝트용으로 개발중인 봇",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x4c2896)
        embed.add_field(name="다양한 기능들 추가 예정", value="시간날 떄마다 추가할 예정입니다.", inline=False)
        embed.add_field(name="GitHub", value="https://github.com/eastminn", inline=False)
        embed.set_footer(text="Bot Made by 김동민#0026, 문의는 DM으로 부탁드립니다 💬", icon_url="https://cdn.discordapp.com/attachments/955360993729449987/955392163158569021/IMG_20220320_042000_013.jpg")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/794866894615085087/956481187780644935/99pk9saw36t7q8t3o0gt.jpg")
        await ctx.send(embed=embed)

    @commands.command(name="청소") # '!청소' 를 입력한다면
    @commands.has_permissions(manage_roles=True, ban_members=True) # 권한이 있는 유저만 실행할 수 있도록 한다.
    async def clear(self,ctx, amount : int):
        await ctx.message.delete() # '!청소 숫자' 메세지는 삭제한다.
        await ctx.channel.purge(limit=amount)
        embed = discord.Embed(title="🧹 청소 기능", description="{} 개의 메세지가 삭제되었습니다.".format(amount),timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x4c2896)
        embed.add_field(name="청소한 사람", value=f"{ctx.author} ( {ctx.author.mention} )", inline=False)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/794866894615085087/956481163353018408/201503181440069692_img_0.gif")
        await ctx.send(embed=embed)
    
    @commands.has_permissions(administrator=True) # 권한이 있는 유저만 실행할 수 있도록 한다.
    @commands.command(name="인증", pass_cotext=True) # '!인증' 을 입력한다면
    async def give_role(self, ctx,nickname : discord.Member, member: discord.Member=None):
        member = member or ctx.message.author
        await member.add_roles(get(ctx.guild.roles, name="유저 😀"))
        embed = discord.Embed(title='💡 인증 기능', description="{} 님이 {} 을 인증하였습니다.".format(ctx.author, nickname), timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x4c2896)
        await ctx.send(embed=embed)


def setup(app): # cog 기능을 위한 코드
    app.add_cog(simple(app))