
#Q1
row = int(input("양의 정수를 입력하세요: "))

for i in range(1, row+1):
    for k in range(1, i+1):
            print(k, end="")
    print()
print("\n")

#Q2

for i in range(5):
    for w in range(5):
        print("*", end="")
    print()
print("\n")
for i in range(5):
    for w in range(5):
        print("*", end="")
    print()
print("\n")
for i in range(5):
    for w in range(5):
        print("*", end="")
    print()
print("\n")

#Q3
row =5

for a in range(5):
    for b in range(5):
        if a==0 or b==0 or b==2 or b==4 or a==2 and b==1 or a==2 and b==3 or a==4 and b==1 or a==4 and b==3:
            print("*", end="")
        else:
            print(" ", end="")
    print()
print("\n")

for i in range(5):
    for n in range(5):
        if n==i :
            print(" ", end="")
        else :
            print("*", end="")
    print()
