import random

# try_count = 0 # 시도 횟수
# st_count = 0 # 스트라이크 카운트
# ba_count = 0 # 볼 카운트
# out_count = 0 # 아웃 카운트
########################################

#리스트 선언
mylist=[1,5,9]

out_count = 0 # 아웃 카운트
try_count = 1 #시도 횟수
st_count = 0 # 스트라이크 카운트

#난수 생성기 0부터 9까지
# ran_1 = str(random.randint(0, 9))
# #중복 없이
# for value in range(3):
#     while ran_1 in mylist:
#         ran_1 = str(random.randint(0, 9))
#     mylist.append(ran_1)
#     #print(*mylist) #확인용
############################################

while True:
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

    # 게임 시도횟수 5이상 #작동불가
    if try_count >= 5:
        try_count+=1
        print("게임횟수 초과")
        break
    # 3 스트라이크 종료
    if strike_count ==3:
        print("승리")
        break
##########################################################

# #3스트라이크 시 종료
# while st_count<3 :
#     st_count = 0
#     ba_count = 0
#     out_count = 0
# #시도 횟수
#     try_count +=1
#     print("시도횟수 {}".format(try_count))
    
# #입력받기
#     num = str(input("정수 3개를 입력 하시오:"))
#     if len(num)== 4:
#         print("정수 3개만 입력하여 주십시오")
#         break
#     else:
#         pass
# ############################################
# #문자열이 3개 일때
#     if len(num) == 3:
#         for i in range(3):
#             for j in range(3):
#                 #리스트 인덱스가 같은 자리면 스트라이크
#                 if num[i]== str(mylist[j]) and i==j:
#                     st_count +=1
#                 #리스트 인덱스가 같은 자리가 아니고, 자리만 다를 경우
#                 elif num[i]== str(mylist[j]) and i!=j:
#                     ba_count +=1
#         #스트라이크 카운트 0 , 볼 카운트 0면 아웃처리
#         if st_count==0 and ba_count==0:
#             out_count+=1 # 아웃 카운트
#             print("Out: ","아웃 {}번".format(out_count))
#             print()
#         #아웃 두번 시 패배
#         elif out_count ==2:
#             print("패배.")
#         #else는 결과값 포맷팅
#         else:
#             output = ""
#             if st_count >0:
#                 output+="{} Strike".format(st_count)
#             if ba_count >0:
#                 output+="{} Ball".format(ba_count)
#             elif try_count >=5:
#                 output+="{} 게임 횟수 초과".format(try_count)
#                 try_count +=1
#                 # break
#             print(output.strip())
#             continue
# ############################################   
# #//안되는거: 게임 횟수 초과시 // 아웃 2번시 종료// 아웃 카운트 올라갈때 중첩












    # elif try_count <4:
    #     print("게임 횟수 초과", "\n", "정답은:",mylist,"입니다.")
    # print("결과:Strike[", st_count,"]ball[", ba_count, "]out[", out_count,"]")
    

