# # def arg(count, avg):
# print("====================")
# print("1. 학생 성적 입력")
# print("2. 학생 목록 출력(입력 순)")
# print("3. 프로그램 종료")

# print("현 입력 데이터 갯수 :")
# print("전체 학생 평균 값 :")
# print("====================")

# stu = "1. 학생 성적 입력"
# lister = "2. 학생 목록 출력(입력 순)"
# ex = "3. 프로그램 종료"

# mylist = []
# number = int(input("번호 선택:"))
# if str(1):
#     input("학번을 입력하세요: ")
#     input("이름을 입력하세요: ")
#     input("국어 성적을 입력하세요: ")
#     input("영어 성적을 입력하세요: ")
#     input("수학 성적을 입력하세요: ")
#     mylist.append()
# print(mylist)

# # 성적 입력
# def Insert(student):
#     name = input("이름을 입력하세요")

#     if (name not in student) == True:
#         mylist = []
#         kor = int(input("국어 성적을 입력하세요"))
#         eng = int(input("영어 성적을 입력하세요"))
#         math = int(input("수학 성적을 입력하세요"))
#         mylist.append(kor+eng+math)
#         #총점
#         score = kor+eng+math
#         #평균
#         averege = score / 3

stcount = []
# ----- 성적 입력 -----
def Insert(student):
    name = input('이름 입력 : ')
    id = input('학번 입력 : ')
    #이름이 딕셔너리 내에 없을경우,
    if (name not in student) == True:

        #성적 입력
        kor =  int(input('국어 성적을 입력하세요 : '))
        eng =  int(input('영어 성적을 입력하세요 : '))
        math = int(input('수학 성적을 입력하세요 : '))
        print('성적이 입력되었습니다.')

        score = kor+eng+math
        avg = round(score/3, 3)
        stcount.append(score)

    #이름이 중복일 경우
    else:
        print('학생이 존재합니다.')
        return Insert(student)
        

    #딕셔너리 Key = Value
    student[id] = [id]
    student[name] = [kor, eng, math, score, avg]
    person = student[name]
    return student


# ----- 성적 출력 -----
def View(student):
    print("=======================================================")
    # print('점수 : [국, 영, 수, 총점, 평균]')
    # print('학번 : [] ')
    
    # 딕셔너리 key, value 출력하기(item)
    for key, value in student.items():
        print(key,':', value)
    print("=======================================================")
        
    return student
def main():
    count = 0
    count2 = []
    #student 딕셔너리 생성
    student = dict()
    # print("====================")
    # print("1. 학생 성적 입력")
    # print("2. 학생 목록 출력(입력 순)")
    # print("3. 프로그램 종료")

    # print("현 입력 데이터 갯수 : ", count)
    # print("전체 학생 평균 값 :", count1)
    # print("====================")

 
    while True:
        print("====================")
        print("1. 학생 성적 입력")
        print("2. 학생 목록 출력(입력 순)")
        print("3. 프로그램 종료")

        print("현 입력 데이터 갯수 : ", count)
        print("전체 학생 평균 값 :", count2)
        print("====================")
        select = int(input("1.입력 2.출력 3.종료 \n"))
        # ----- 성적 입력 -----
        if select == 1:
            student = Insert(student)
            count += 1
            count2.append(stcount)

        # ----- 성적 출력 -----
        elif select ==2:
            student = View(student)
        
        elif select ==3:
            print("종료")
            break

main()





