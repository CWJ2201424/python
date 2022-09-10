#call-by-value는 값이 복사가 되어 전달 됨

def bar(a):
    a+=3 # 의미 없음
value = 1 # 이 값이 복사
bar(value)
print(value)