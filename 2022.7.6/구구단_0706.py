# 메뉴 출력
while True:
    print("-------------------")
    print("1. 구구단 출력")
    print("2. 프로그램 종료")
    print("-------------------")
#메뉴 번호 선택
    in_number= int(input("메뉴 번호 입력:"))

# 메뉴 1 = 구구단 출력, 2 = 프로그램 종료
# 1이면 구구단 단 입력 / 2이면 종료 / 0이면 다시 질문.
    if in_number == 1:
        u= int(input("출력할 구구단의 단을 입력하세요.: "))
        
    elif in_number == 2:
        print("이용해주셔서 감사합니다.")
        exit()
    elif in_number == 0:
        print("잘못 입력 하셨습니다. 다시 입력하세요")
        break
#구구단 단수 입력시 2~9사이가 아닌 범위 외의 정수는 에러 메세지후 다시 질문.
    i=1
    errer_msg="올바른 값을 입력 하세요."
    if u<=1 or u>=10 :
        print(errer_msg, "\n", "\t", "2~9사이 정수를 입력해주세요.")
#구구단 2~9까지 맞는 값을 대입 시 in_number X 1~9 까지 반복 후 다시 질문.
    else:
        while i<10:
            i= i+1
            print(u, "X", i, "=", u*i)
            
            
    


