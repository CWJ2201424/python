row = 5
col = 5
#세로 루프
for row_count in range(row):
    #가로 루프
    for col_count in range(col):
        #가로 index == 세로 인덱스 "*" 출력 
        #-> row_count == col_count 
        #아니면 " " 출력

        #가로 인덱스 + 세로 인덱스 == row-1 ->4니까 변수 5에서 -1값 "*"출력
        #->row_count + col_count == row-1 
        #아니면 " " 출력

        #row_count ==0 또는 row_count == row -1 이면 "*" 출력
        if row_count == col_count    or row_count + col_count == row-1 or     row_count ==0 or row_count == row -1 :
            print('*', end="")
        else:
            print(' ', end='')
    print()