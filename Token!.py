import discord
import bs4

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('\help'):
        embed = discord.Embed(title="Prefix는 \입니다!", description="\help = 명령어 리스트를 보여준다.\n \smile = 웃는 이모지를 보내준다.\n \hi = 제온봇이 안녕이라고 인사한다.\n ", color=0x62c1cc) # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다
        
        await message.channel.send(embed=embed) # embed를 포함 한 채로 메시지를 전송합니다.
        await message.channel.send("명령어 목록입니다!", embed=embed)

        await client.change_presence(game=discord.Game(name="\help로 명령어를 알아보세요!", type=1))


        if message.content.startswith('\hi'):
         await message.channel.send('안녕하세요!')

        if message.content.startswith('\smile'):
         await message.channel.send(':smile:')

client.run('NzM2MTA0OTEyMTk4NDM0ODY5.Xxp9Hw.oNoTv2sEfYa8z3ZPcAr1DlNGABI')
                         
