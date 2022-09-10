num = int(input("라인 넘버를 입력하세요: "))

for i in range(num) :
    if i <= num//2 :
        for j in range(i+1) : 
            print("*", end="")
    else:
        for j in range(num-i) :
            print("*", end="")


    print()