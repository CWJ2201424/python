#call-by-reference는 메모리 주소값이 전달 되어지고 그 주소값 뒤에 붙임

def foo(a): # 0xffaa 값 뒤에 append 1값이 더해져서 나옴
    a.append(1)
value = [2, 3] #ex) 0xffaa

foo(value)
print(value)