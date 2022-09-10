import random

numList = []
count1 = 0
max = -1
max1 = -1
max2 = -1
max3 = -1
max4 = -1
max5 = -1
min = 100
min1 = 100
min2 = 100
min3 = 100
min4 = 100
min5 = 100
n = 5

# 랜덤함수생성(25개 중복x)
while len(numList) < 25:            # 리스트 갯수 25개면 정지
    count1 = 0                      # 카운트 0으로
    while count1 < 5:               # 카운트5개면 정지
        num = random.randint(1,50)  # 1,50 랜덤함수생성
        if num not in numList:      # 리스트안에 중복값이없으면
            numList.append(num)     # 해당값 입력
            count1 += 1             # 카운트 +

# 출력용
for a in range(len(numList)):
    if a%5 == 0:
        print()
    print("\t",numList[a],end="\t")
print()

# 5x5 비율로 만들기
def divide_list(l, n): 
    # 리스트 l의 길이가 n이면 계속 반복
    for i in range(0, len(l), n): 
        yield l[i:i + n]
result = list(divide_list(numList, n))

# 최소, 최대 <1열>
for a in range(5):
    value = result[a][0]
    if max1 < value:
        max1 = value

    if min1 > value:
        min1 = value
# 최소, 최대 <2열>
for a in range(5):
    value = result[a][1]
    if max2 < value:
        max2 = value

    if min2 > value:
        min2 = value
# 최소, 최대 <3열>
for a in range(5):
    value = result[a][2]
    if max3 < value:
        max3 = value

    if min3 > value:
        min3 = value
# 최소, 최대 <4열>
for a in range(5):
    value = result[a][3]
    if max4 < value:
        max4 = value

    if min4 > value:
        min4 = value
# 최소, 최대 <5열>
for a in range(5):
    value = result[a][4]
    if max5 < value:
        max5 = value

    if min5 > value:
        min5 = value
print()


print("---열---")
print("최소값 :",
min1,"\t\t",min2,"\t\t",min3,"\t\t",min4,"\t\t",min5)

print("최대값 :",
max1,"\t\t",max2,"\t\t",max3,"\t\t",max4,"\t\t",max5)

# 리스트 열 부분 행으로 재정렬
result1 = [result[0][0],result[1][0],result[2][0],result[3][0],result[4][0]]
result2 = [result[0][1],result[1][1],result[2][1],result[3][1],result[4][1]]
result3 = [result[0][2],result[1][2],result[2][2],result[3][2],result[4][2]]
result4 = [result[0][3],result[1][3],result[2][3],result[3][3],result[4][3]]
result5 = [result[0][4],result[1][4],result[2][4],result[3][4],result[4][4]]

# 재정렬한 리스트 각각 오름차순 정렬
result1.sort()
result2.sort()
result3.sort()
result4.sort()
result5.sort()

# 위 리스트 합치기
new_result = result1 + result2 + result3 + result4 + result5

# 정렬한 리스트 2, 7, 12, 17, 22 번째 자리 출력(중간값)
print("중간값 :",end=" ")
for a in range(2, 23, 5):
    print(new_result[a],end="\t\t"" ",)
print()

max1 = -1
max2 = -1
max3 = -1
max4 = -1
max5 = -1
min1 = 100
min2 = 100
min3 = 100
min4 = 100
min5 = 100



# 최소, 최대 <1행>
for a in range(5):
    value = result[0][a]
    if max1 < value:
        max1 = value

    if min1 > value:
        min1 = value
# 최소, 최대 <2행>
for a in range(5):
    value = result[1][a]
    if max2 < value:
        max2 = value

    if min2 > value:
        min2 = value
# 최소, 최대 <3행>
for a in range(5):
    value = result[2][a]
    if max3 < value:
        max3 = value

    if min3 > value:
        min3 = value
# 최소, 최대 <4행>
for a in range(5):
    value = result[3][a]
    if max4 < value:
        max4 = value

    if min4 > value:
        min4 = value
# 최소, 최대 <5행>
for a in range(5):
    value = result[4][a]
    if max5 < value:
        max5 = value

    if min5 > value:
        min5 = value
print()

# result 리스트 오름차순 정렬
print("---행---")
print("최소값  최대값  중간값")

# 리스트 행 부분 재정렬
result6 = [result[0][0],result[0][1],result[0][2],result[0][3],result[0][4]]
result7 = [result[1][0],result[1][1],result[1][2],result[1][3],result[1][4]]
result8 = [result[2][0],result[2][1],result[2][2],result[2][3],result[2][4]]
result9 = [result[3][0],result[3][1],result[3][2],result[3][3],result[3][4]]
result10 = [result[4][0],result[4][1],result[4][2],result[4][3],result[4][4]]


# 재정렬한 리스트 각각 오름차순 정렬
result6.sort()
result7.sort()
result8.sort()
result9.sort()
result10.sort()

# 위 리스트 합치기
new_result1 = result6 + result7 + result8 + result9 + result10

# 최대,최소값 출력 및 중간값 해당위치 출력
print(" ",min1,"\t", max1,"\t", new_result1[2])
print(" ",min2,"\t", max2,"\t", new_result1[7])
print(" ",min3,"\t", max3,"\t", new_result1[12])
print(" ",min4,"\t", max4,"\t", new_result1[17])
print(" ",min5,"\t", max5,"\t", new_result1[22])
print()
print("---전체---")

# 전체 최소,최대
for value in numList:
    if max < value:
        max = value

    if min > value:
        min = value
print("최소값 : ", min)
print("최대값 : ", max)
# 전체리스트 오름차순정렬
result.sort()
# 전체리스트 중간자리출력
print("중간값 : ", result[2][2])