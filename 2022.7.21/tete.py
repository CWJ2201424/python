# # 합계 평균
# mylist=[]
# inputvalue=[0]*5
# for index in range(5):
#     inputvalue[index]= int(input(str(index +1) + "번째 숫자 입력: "))
#     mylist.append(inputvalue)

# result = print("합계:", sum(inputvalue))

# result_1 = 0
# for vaule_1 in inputvalue:
#     result_1+=vaule_1
# print("평균:", result_1 / len(inputvalue))


# # 정수 입력 양수 음수 판별

# while True:
#     inputing = int(input("정수를 입력하세요: "))
#     if inputing <0:
#         print("음수 입니다.")
#     elif inputing > 0:
#         print("양수 입니다.")
#     else:
#         break


#별 #x
num = 5
for row in range(num):
    for col in range(num-row):
        print("*", end="")
    if row == 1:
        print(" ", end="")
        row+=1
    print()

# # 1~100까지 양의 정수 3이 포함된 정수 출력
# for i in range(1, 101):
#     if "3" in str(i):
#         print(i)

# 특수문자 개수 글자수 단어수 카운트 프로그램 #x
# 특문: ! | . | , |
myList ="!! hello world, it is awesome day."

# print("특수문자 수:")
# print("단어 수")
# print("특수문자 제외 글자 수")