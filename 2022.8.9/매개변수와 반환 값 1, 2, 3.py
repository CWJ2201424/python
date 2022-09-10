# # 매개 변수와 반환 값은 필요에 따라 생략 가능 (1)

# # 매개 변수와 매개 변수가 없는 함수 예제
# def printHello():
#     print("Hello")

# printHello() # Hello 

####################

# # 함수 반환 값 예제 (2)

# # 평균을 구하는 함수
# def average(arglist):
#     sum = 0
#     for value in arglist:
#         sum += value
#     return sum/len(arglist)

# mylist = [7, 8, 6, 8]

# #average 함수 호출 후 반환 값을 avg 변수에 저장
# avg = average(mylist)

# print(avg)

#####################

# 파이썬은 함수의 반환 값이 두 개 이상일 경우 Tuple 형으로 반환

def sumAndMultiply(argA, argB):
    resultSum = argA + argB
    resultMultiply = argA * argB
    # 반환 값이 두 개 이상일 경우 Tuple형으로 반환
    # Tuple은 LIST 와 같음, 단 원소 내용은 변경 불가
    return resultSum, resultMultiply
# sumAndMultiply 함수 호출 후 Tuple 형으로 반환 값 획득
# 함수 한개면 def 값 sum값과 multiply값에 a, b 차례로 들어가서 계산
result = sumAndMultiply(2, 3)
print(result) #(5, 6 = a+b / a*b)

#함수 두개면 def 값 sum값과 multiply값에 각각 들어가 a+b / a*b 따로 따로 계산 후 출력
sum, multiply = sumAndMultiply(4, 5)
print(sum, multiply) # (9, 20 = a+b / a*b) 