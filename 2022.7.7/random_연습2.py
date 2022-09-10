import random 

# 0이상 5미만의 실수 출력
# for value in range(10):
#     num = random.random() *5
#     print(num)

# 0이상 5미만의 정수 출력
# for value in range(10):
#     num = int(random.random() *5)
#     print(num)

# 0이상 11미만에서 전체식에 -5 더해주면 이 식은 -5이상 6미만이 된다.
# 정수 값 출력
for value in range(50):
    num = int(random.random() *11)-5
    print(num)

# -5이상 5이하.
# for value in range(50):
#     num = random.randint(-5, 5)
#     print(num)