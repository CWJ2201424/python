# 줄 수를 입력
in_line = str(input("입력 문자열의 줄(Line) 수를 입력하세요!: "))

# N 번째 라인의 문자열을 입력하세요. + 문자 열로 리스트에 추가  
inputline = []
U = 1
for i in range(int(in_line)):
    print(("{} 번째 라인의 문자열을 입력하세요: ".format(U)))
    inputline_1 = input()
    inputline.append(inputline_1)
    U+=1
print(inputline)

# 검색할 문자열 입력.
searchstring_1 = str(input("검색 할 문자열을 입력하세요.: "))

if searchstring_1 in inputline:
    print(searchstring_1, "를 찾았습니다.")

else:
    print("찾을 수가 없습니다. ", searchstring_1)
        
#inputline = ["aaa", "hello", "cara"]

#돌면서 원소 원하는거 출력

for row in range(len(inputline)):
    for col in range(len(inputline[row])):
        print(inputline[row][col],"/", end=" ")
        # searchstring_1 += inputline[row][col]



        #dhello / hellod/ dhellod 판별




        
    # if row == col:
    #     print("1")
    #     print(inputline[row][col],"/", end=" ")
    # print()







        #찾으면 라인 수 // 검색된 횟수 // 총 단어 수 출력
        # print("검색된 라인 수")
        # print("검색된 횟수")
        # print("총 단어 수")
        
# [['dd', 'ff', 'gg'],['dd', 'ff'],['dd']]