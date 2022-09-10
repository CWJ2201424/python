value = 3 # 전역변수 (global variable)

def bar():
    value = 4 #지역변수 (local variable)
    print(value) # 4

print(value) # 3

bar()

print(value) # 3