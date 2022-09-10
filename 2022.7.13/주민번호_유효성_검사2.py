#입력 받기


myString = input("주민 번호를 입력하세요. (13자리 - 제외): ")
#checklist = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]

if len(myString)==13:
    total=0
    for i in range(12):
        multi=int(myString[i])*(i%8+2)
        total+=multi
        # print('{}번째 합계는{}이다.'.format(i+1, multi))
    total= (11-total%11) %10

    if int(myString[12])==total:
        print("유효")
    else: 
        print("유효 x")
else:
    print("다시 입력")
    
    