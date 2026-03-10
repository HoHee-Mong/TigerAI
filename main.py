import discord
import os
from dotenv import load_dotenv

# 비밀 금고(.env) 문 열기
load_dotenv()
# 금고 안에서 토큰 꺼내오기
TOKEN = os.getenv('DISCORD_TOKEN')

# 봇 권한 설정
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'짜잔! {client.user} 봇이 온라인 되었습니다!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '안녕':
        await message.channel.send('반가워! 난 승호가 만든 천재 봇이야! 🤖')

# 꺼내온 토큰으로 봇 실행! (이제 코드에 비밀번호가 안 보여!)
client.run(TOKEN)