allStudendsList=[]
allStudendsList1=[]

# 일단
def allStudends():
    sum=0
    id=input('학번을 입력하세요 : ')

    nick=input('이름을 입력하세요 : ')

    kor=input('국어 성적을 입력하세요 : ')

    sum+=int(kor)
    eng=input('영어 성적을 입력하세요 : ')

    sum+=int(eng)
    math=input('수학 성적을 입력하세요 : ')

    sum+=int(math)

    avg=round(sum/3, 1)
    
    allStudendsList.append(['id : ', id ,'name : ', nick, 'kor : ', kor, 'end : ', eng, 'math : ', math, 'sum : ', sum, 'avg : ', avg])

    allStudendsList1.append(['id : {0}, name : {1}, kor : {2}, eng : {3}, math : {4}, sum : {5}, avg : {6}'.format(id, nick, kor, eng, math , sum, avg)])

count=0
allAvg=0
while True:
    b=0 
    print('='*26)
    print('1. 학생 성적 입력')
    print('2. 학생 목록 출력(입력 순)')
    print('3. 프로그램 종료')
    print()
    print('현 입력데이터 갯수 : {0}'.format(count))
    print('전체 학생 평균 값 : {0}'.format(round(allAvg, 2)))
    print('='*26)

    num=int(input('실행 프로그램 선택 : '))
    print()
    if num==1:
        allStudends()
        count+=1

    for i in range(count):
        b+=allStudendsList[i][-1]
    allAvg=b/count

    if num==2:
        for i in range(count):
            print(allStudendsList1[i])
    
    if num==3:
        print('프로그램 종료')
        break;


