import random

# try_count = 0 # 시도 횟수
# st_count = 0 # 스트라이크 카운트
# ba_count = 0 # 볼 카운트
# out_count = 0 # 아웃 카운트
########################################

#리스트 선언
mylist=[]

out_count = 0 # 아웃 카운트
try_count = 0 #시도 횟수
st_count = 0 # 스트라이크 카운트

#난수 생성기 0부터 9까지
index = random.randint(0, 9)
#중복 없이
for value in range(3):
    while index in mylist:
        index = random.randint(0, 9)
    mylist.append(index)
    print(*mylist) #확인용
############################################

while True:
    #시도 횟수
    try_count +=1
    print("시도횟수 {}".format(try_count))

    # 정수 3개 입력
    inputValue = [0]*3

    for index in range(3):
        inputValue[index] = int(input(str(index + 1) + "번째 값을 입력 하세요"))

    ball_count = 0
    strike_count = 0
    
    # 볼, 스트라이크 판별
    for index in range(3):
        if inputValue[index] == mylist[index]:
            # 스트라이크
            strike_count += 1

        elif inputValue[index] in mylist:
            # 볼
            ball_count += 1
            #시도 횟수 초과시 정답 알려준후 스톱
        if try_count == 4:
            print("게임횟수 초과")
            print("정답은: ", *mylist, "입니다.")
            break

    # 삼진 또는 볼+스트라이크 현황 출력
    if ball_count == 0 and strike_count == 0:
        print("삼진")
        out_count += 1
    else:
        print("Strike : ", strike_count, " Ball : ", ball_count)

    # 프로그램 종료
    # 삼진 2번
    if out_count >= 2:
        print("삼진 2번 프로그램 종료")
        break

    # 3 스트라이크 종료
    if strike_count ==3:
        print("승리")
        break