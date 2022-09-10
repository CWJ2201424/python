# 키보드로 부터 N개의 정수를 입력 받아 리스트에 저장

def listsave(argnumberinput):
    mylist = []
    for i in range(argnumberinput):
        inputer = input(str(i + 1) + "번째 정렬:")
        mylist.append(int(inputer))

    return mylist

# 리스트에 저장된 정수 값을 오름 차순으로 정렬
def mybubblesorting(alist, blist= True):
    for aCount in range(len(alist)-1):
        # 맨 마지막 값은 판단 된거니 1개 뺌
        for bCount in range(len(alist) - aCount - 1):
            # bCount가 bCount +1 보다 크면 bCount + 1(blist) 자리와 바꿈
            # 변수 선언
            kresult = \
                alist[bCount] > alist[bCount + 1] if blist else alist[bCount] < alist[bCount +1]

            if kresult:
                # 비교시 후자가 크면 바꿈
                temp = alist[bCount + 1]
                alist[bCount + 1] = alist[bCount]
                alist[bCount] = temp
                
# # print(listsave(5))
# print(mybubblesorting([listsave]))
    
# 함수 하나 줘서 저장공간 하나 설정 후 저장
item = listsave(5)
# 정렬(함수) 하는거
mybubblesorting(item)
# 정렬한거 출력
print(item)




# mylist =""" []
# N = 5
# for i in range(N):
#     inputer = input(str(i + 1) + "번째 정렬:")
#     mylist.append(int(inputer))""" == item = listsave(5)

# for aCount in range(N - 1):
#     for bCount in range(N - aCount - 1):
#         if mylist[bCount] > mylist[bCount + 1]:
#             temp = mylist[bCount + 1]
#             mylist[bCount + 1] = mylist[bCount]
#             mylist[bCount] = temp 
# print(mybubblesorting([listsave])) ==>
# print(for aCount in range(N - 1):
#     for bCount in range(N - aCount - 1):
#         if mylist[bCount] > mylist[bCount + 1]:
#             temp = mylist[bCount + 1]
#             mylist[bCount + 1] = mylist[bCount]
#             mylist[bCount] = temp)) ==> 이런거라 아예 틀림