#Q1

#while 문은 boolean형 이다.

num = int(input("정수 입력: "))

a=0

while a<num:
    a=a+1
    b=0
    while b<a:
        b=b+1
        print(b, end="")
    print()

#Q2

a=0

while a<=4:
    a=a+1
    print("*", end="")
    b=0
    while b<4:
        b=b+1
        print("*", end="")
    print()
print("\n")
a=0

while a<=4:
    a=a+1
    print("*", end="")
    b=0
    while b<4:
        b=b+1
        print("*", end="")
    print()
print("\n")
a=0

while a<=4:
    a=a+1
    print("*", end="")
    b=0
    while b<4:
        b=b+1
        print("*", end="")
    print()

#Q3
a=0

while a<=4:
    a=a+1
    b=0
    while b<5:
        b=b+1
        if b==0 or a==2 and b==2 or a==2 and b==4 or a==4 and b==2 or a==4 and b==4 :
            print(" ", end="")
        else :
            print("*", end="")
    print()
print("\n")

a=0
while a<=4:
    a=a+1
    b=0
    while b<=4:
        b=b+1
        if a==1 and b==1 or a==2 and b==2 or a==3 and b==3 or a==4 and b==4 or a==5 and b==5 :
            print(" ", end="")
        else :
            print("*", end="")
    print()

