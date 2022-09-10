#2201424 최원준


#range 함수의 기본적인 개념을 알 수 있다.
#*-*-이 세로로 출력되고 마지막 done 출력 후 탈출

i = 20

for i in range(10):
    print("*")
    print("-")

print("done")
'============================'
#세로 5개 x 가로 5개 출력 for 문 1개 이용 ⑴

for i in range(1, 26):
    print("*", end=' ')

    if i % 5 == 0:
        print()
'============================'
#세로 5개 x 가로 5개 출력 for 문 2개 중첩 이용 ⑵
for i in range(5): 
    for j in range(5):
        print("*", end=' ')
    
    print()
'============================'
#세로 5번 반복 + 순서 역순 + 가로 5번 반복 + 공백란 추가

row = 10

for a in range(row):   
    for b in range(row-a-1):
        print(" ", end=' ')
    for c in range(5):
        print("*", end=' ')
    print()

'============================'
#공란 피라미드

n = int(input())
line = n * 2 - 1
star = '*'
space = ' '
for i in range(n, 0, -1):
    if i == n:
        print(space * (line // 2), end = '')
        print(star)
    elif i == 1:
        print(star*line)
    else:
        print(space * (i - 1) + star, end = '' )
        print(space * (line - i * 2) + star)  
'============================'

n = 5
for i in range(1, n+1):
    
    for j in range(n+1-i):
        print('', end=" ")
    for j in range(2*i-1):
        print('*', end=" ")
    print()

