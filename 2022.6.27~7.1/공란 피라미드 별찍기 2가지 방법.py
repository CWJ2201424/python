#첫번째 방법

row = 5
#range 값은 0~4까지 n-1값
for value in range(row): # 세로로 5번 반복
    for i in range(row - value - 1): # 공백으로 밀기
        print(' ', end='')
        
    # * 출력
    # 수식 : 2 X N - 1
    # N : 라인넘버, 1 -> 5
    # * 출력 횟수/라인넘버 : 1, 3, 5, 7, 9   
    for j in range(2*value + 1): # 가로로 * 5번 반복
        #출력시 +1은 2*value가 0이면 출력 오류 생기니 있는것
        #거기서 range(1)은 0이 값이니 if로 가는것.
        # 처음 또는 끝 반복 또는 마지막 줄일 경우 "*"를 출력
        # 그 이외는 " " 출력
        if j == 0 or j == 2*value or value == row -1:
            #value == row-1 은 9까지 라인넘버가 출력되니 때문
            print("*",end="")
        else:
            print(" ",end="")
            
    
    print()


#두번째 방법 
n = 5
line = n * 2 - 1
star="*"
space=' '

for i in range(n, 0, -1):
    if i == n:
        print(space * (line//2), end='')
        print(star)
    elif i == 1:
        print(star * line)
    else:
        print(space * (i - 1) + star, end='')
        print(space * (line - i * 2) + star)
    
    
    