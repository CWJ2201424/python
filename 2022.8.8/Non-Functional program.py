# N개의 정수를 입력 받아 오름 차순으로 정렬

N = 5

# 키보드로 부터 N개의 정수를 입력 받아 리스트에 저장
mylist = []
for i in range(N):
    inputer = input(str(i + 1) + "번째 정렬:")
    mylist.append(int(inputer))

# 리스트에 저장된 정수 값을 오름 차순으로 정렬
# for 문 2번 돌려 판단 
for aCount in range(N - 1):
    # 맨 마지막 값은 판단 된거니 1개 뺌
    for bCount in range(N - aCount - 1):
        if mylist[bCount] > mylist[bCount + 1]:
            # 비교시 후자가 크면 바꿈
            temp = mylist[bCount + 1]
            mylist[bCount + 1] = mylist[bCount]
            mylist[bCount] = temp
# 리스트 값 출력
print(mylist)