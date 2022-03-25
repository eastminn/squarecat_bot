from urllib import response
import discord, asyncio, datetime, pytz
import requests
from bs4 import BeautifulSoup
from discord.ext import commands
from discord.utils import get

client = commands.Bot(command_prefix='!')

class corona(commands.Cog):
    def __init__(self, app):
        self.app = app 

    @commands.command(name="코로나")
    async def crawl(self, ctx):
        url = "https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query=%EC%BD%94%EB%A1%9C%EB%82%9819"
        response = requests.get(url)  # get 방식으로 웹 정보 받아오기
        response_code = int(response.status_code)  # 응답 코드 받기
        
        if response_code == 200:  # 정상 작동(코드 200 반환) 시
            soup = BeautifulSoup(response.content, 'lxml')
            
        else:  # 오류 발생
            await ctx.send("웹 페이지 오류입니다.")
            
        # element
        new = soup.find("div", {"class":"status_info"}).findAll("p", {"class":"info_num"})
        today_infection = new[0].text # 일일 감염자
        critical_condition = new[1].text # 재원 위중증
        new_Hospitalization = new[2].text # 신규 입원
        today_died = new[3].text # 일일 사망자

        # 가독성을 위한 임베드
        embed = discord.Embed(title="🧬 코로나 19", description="http://ncov.mohw.go.kr/ 의 정보를 가져옵니다.",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x4c2896)
        embed.set_author(name="코로나 바이러스 감염증 - 19 (COVID-19)", url="http://ncov.mohw.go.kr/", icon_url="https://cdn.discordapp.com/attachments/779326874026377226/789094221533282304/Y5Tg6aur.png")
        embed.add_field(name="일일 확진자", value="{}명".format(today_infection), inline=True)
        embed.add_field(name="재원 위중증", value="{}명".format(critical_condition), inline=True)
        embed.add_field(name="신규 입원", value="{}명".format(new_Hospitalization), inline=True)
        embed.add_field(name="일일 사망자", value="{}명".format(today_died), inline=True)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/956550003755741245/956610477184659486/9068ce115fb4499b9fc404664274e95e.png")
        embed.set_footer(text="자세한 정보는 위의 프로필 버튼의 사이트를 방문해주세요.", icon_url="https://cdn.discordapp.com/attachments/779326874026377226/789098688315654164/Flag_of_South_Korea.png")
        await ctx.send(embed=embed)

def setup(app): # cog 기능을 위한 코드
    app.add_cog(corona(app))
    
    