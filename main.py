import discord
import os
from dotenv import load_dotenv
from sklearn.linear_model import LinearRegression

# ==========================================
# ☕ 1번 AI 뇌: 커피 수면 시간 예측기
# ==========================================
print("1번 AI: 커피 데이터 공부 중...")
coffee_x = [[0], [1], [2], [3], [4]]
coffee_y = [8, 7, 6, 5, 4]

coffee_model = LinearRegression()
coffee_model.fit(coffee_x, coffee_y)

# ==========================================
# ⚔️ 2번 AI 뇌: 게임 데미지 예측기 (승희가 직접 만듦!)
# ==========================================
print("2번 AI: 게임 데미지 규칙 공부 중...")
game_x_data = [[10], [20], [30], [40], [50], [60]]
game_y_data = [50, 60, 70, 80, 90, 100]

game_model = LinearRegression()
game_model.fit(game_x_data, game_y_data)

print("모든 AI 공부 완료! 봇을 깨웁니다!")

# ==========================================
# 🤖 디스코드 봇 설정 및 실행
# ==========================================
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

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
        await message.channel.send('반가워! 난 승희가 만든 천재 AI 봇이야! 🤖')

    # 1. 커피 명령어
    if message.content.startswith('!커피 '):
        try:
            cup_count = int(message.content.split(' ')[1])
            question = [[cup_count]]
            predict_result = coffee_model.predict(question)
            sleep_time = round(predict_result[0], 1)
            await message.channel.send(f'☕ 커피를 {cup_count}잔 마셨다고? 오늘은 약 **{sleep_time}시간** 잘 수 있을 것 같아!')
        except ValueError:
            await message.channel.send('명령어가 틀렸어! "!커피 3" 처럼 숫자만 정확히 적어줘!')

    # 2. 게임 데미지 명령어 (승희 작품!)
    if message.content.startswith('!공격 '):
        try:
            atk = int(message.content.split(' ')[1])
            question = [[atk]]

            # 승희가 만든 game_model이 활약하는 부분!
            predict_result = game_model.predict(question)
            damage = round(predict_result[0])

            await message.channel.send(f'⚔️ 공격력이 {atk}라고? 내 계산에 따르면 데미지는 **{damage}** 정도 뜰 거야!')
        except ValueError:
            await message.channel.send('명령어가 틀렸어! "!공격 100" 처럼 숫자만 정확히 적어줘!')

client.run(TOKEN)