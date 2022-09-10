# a=1=="구구단 출력"
# b=2=="프로그램 종료"

# num=int(input())
# if a:
#     print("출력할 구구단의 단을 입력하세요.", int(input()))
# elif b:
#     print("프로그램 종료", )


def print_menu():
    print("-------------------------")
    print("1. 구구단 출력")
    print("2. 프로그램 종료")
    print("-------------------------")
    
    in_number= int(input("번호 입력."))

    if in_number == 1:
        print("출력할 구구단의 단을 입력하세요.")
    elif in_number == 2:
        print("프로그램 종료")
        exit()
    else:
        print("잘못 입력 하셨습니다. 다시 입력하세요.")
while True:
    
