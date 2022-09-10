# positional argment #앞 자리 부터 차례대로 들어감
def foo (a, b, c):
    print(a, b, c)
foo(1, 2, 3) # 1, 2, 3
# keyword argment # 선언해서 들어감
def bar (a, b, c):
    print(a, b, c)
foo(b=2, a=1, c=3) # 1, 2, 3
# default argment # 비어있는 값에 들어감
def han (a, b=2, c=3):
    print(a, b, c)
han(1) # 1, 2, 3
# arbitrary positional argments #튜플 타입
def pos(*a):
    print(type(a))
    for value in a:
        print(value)

pos(1, 2, 3)
# arbitrary keyword argments # 딕셔너리 타입
def fox(**a):
    print(type(a))
    for k, v in a.items():
        print(k, v)
        
fox(name="choi", gender="male")