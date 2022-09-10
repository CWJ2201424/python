import random

#리스트 선언
mylist = [] 
#1~20 까지 랜덤 난수 돌리기
for value in range(20):
    mylist.append(random.randint(1, 20)) 

#난수 돌린 리스트 출력
for value in range(1):
    print("랜덤 값: ", "\n", "\t", *mylist)

#최소 값 출력    
a= mylist
small = a[0]
for value in a:
    if value< small:
        small = value
print("최소 값:", small)

#최대 값 출력
a= mylist
large = a[0]
for value in a:
    if value > large:
        large = value
print("최대 값:", large)

#평균 값 출력 
arr_1=mylist

result_1 = 0
for vaule_1 in arr_1:
    result_1+=vaule_1
print("평균:", result_1 / len(arr_1))

#합계 출력
arr_2 = mylist
result_2 = print("합계:", sum(arr_2))

#중복 값 / 중복 횟수 출력

a_2 = mylist

a_1 ={}

for i in a_2:
    try:
        a_1[i] += 1
    except:
        a_1[i] = 1
print("중복 값:" , " ", "중복 갯수", "\n" , a_1)

#구간별 히스토그램

print("구간별 히스토그램", "\n")
aa=mylist
while True:
    for aa in mylist:
        if aa[0:6] < 6:
            print("1~5:", "*" )
        elif aa[6:11]< 11:
            print("6~10:", "*" )
        elif aa[11:16]< 16:
            print("11~15:", "*" )
        else:
            print("15~20:", "*" )
            break
    print()

