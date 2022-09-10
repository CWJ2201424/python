# 검색어 : hello
# dhello dhellod hellod
# hello
# 입력 값

num = int(input("줄 수를 입력 하세요"))

textList = []

# 문장 입력
for index in range(num):   
    textList.append(input(str(index + 1) + "번째 문장을 입력 하세요"))

# 검색어 입력
findWord = input("검색 단어를 입력 하세요")


if findWord in textList:
    print(findWord, "를 찾았습니다.")

else:
    print("찾을 수가 없습니다. ", findWord)

for row in range(num):    
    stateIndex = 0    
    previousChar = ""    
    nextChar = ""
    stringer = 0
    for col in range(len(textList[row])):        
        nextChar = "" if col == (len(textList[row]) - 1) else textList[row][col+1]         
        #print("prev : ", previousChar, " cur : ", textList[row][col], " next : ", nextChar)        
    # 매칭 시작        
        if textList[row][col] == findWord[stateIndex] and stateIndex == 0:        
            stateIndex += 1  
            stringer += 1     
        # 매칭 중        
        elif textList[row][col] == findWord[stateIndex]:      

            # 값 검색 완료        
            if stateIndex == (len(findWord) - 1):      
                print("검색 된 라인 수 ", row, col)
                print("검색된 횟수 :", num)
                print("단어 수 :", stringer)
                stateIndex = 0           
            # 매칭 계속        
            else:        
                stateIndex += 1                
        # 매칭 실패        
        else:        
            stateIndex = 0
            stringer = 0

    previousChar = textList[row][col]