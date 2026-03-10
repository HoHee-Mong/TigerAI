# 천재들이 만든 AI 뇌(LinearRegression) 가져오기
from sklearn.linear_model import LinearRegression

# 1. 데이터 준비 (AI는 문제를 '서랍장' 모양으로 묶어서 받는 걸 좋아해!)
x_data = [[1], [2], [3], [4], [5]]  # 문제 (대괄호가 두 개씩 들어간 거 주의!)
y_data = [2, 4, 6, 8, 10]           # 정답

# 2. 빈 AI 모델(뇌) 준비하기
model = LinearRegression()

# 3. AI 학습시키기 (가장 중요한 마법의 단어: fit)
print("AI가 열심히 공부하는 중...")
model.fit(x_data, y_data) # "이 문제와 정답을 보고 규칙을 찾아내!"
print("공부 완료!")

# 4. AI에게 시험 보기
# 이번엔 6, 7, 8 세 개의 문제를 한꺼번에 던져볼게!
test_question = [[6], [7], [8]]
answer = model.predict(test_question)

print(f"AI가 돌려준 상자 전체 모습: {answer}")
print(f"첫 번째 문제(6)의 정답: {answer[0]}")
print(f"두 번째 문제(7)의 정답: {answer[1]}")
print(f"두 번째 문제(8)의 정답: {answer[2]}")