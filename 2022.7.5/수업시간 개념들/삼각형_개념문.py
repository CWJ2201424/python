
#/가 나오면 내부에서 실수로 치환, //도 실수형, %도 실수형
#print(type(4/2)) or print(type(4//2.0)) or print(type(4%2.0))

# for v in range(5):
#     print("/", v /2)
#     print("//", v /2)
#     print("%", v /2)


# num 5
# *
# **
# ***
# **
# *

num =5 
median = num //2+1

# [0, 1, 2, 3, 4]
for row_num in range(num):
    # * 증가 반복문 : row_num < median [0, 1, 2]
    if row_num < median :
        for star_count in range(row_num + 1): #[1, 2, 3]
            print("*", " ", end="")
    # * 감소 반복문
    else:
        for star_count in range(num-row_num): #[]
            print("*", " ", end="")

    print()