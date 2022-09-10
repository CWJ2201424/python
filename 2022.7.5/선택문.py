from msilib import Table


Table = 7
for j in range(Table):
    num = int(input("정수를 입력 해주세요. : "))
    i=0

    if num>0 :
        print( i+1 , "번째 " , "입력 값은 = " , num)
    else:
        print("1이상 양수를 입력해주세요.")
    for w in range(1):
        if num % 7 == 0 :
            print("\t", "7의 배수 입니다.")
        elif num % 3 == 0 :
            print("\t", "3의 배수 입니다.")
    print()

