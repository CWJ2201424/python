import turtle as t

#원 만들기

# i 는 원 50번 반복
i = 60
t.bgcolor("sky blue") # 백그라운드 컬러 블랙 지정
t.color("yellow") # 선 노란색 지정
t.speed(0) # 그리는 속도 최대속도 지정

for k in range(i): #60번 반복
    t.circle(80) # 반지름 80픽셀 원 출력
    t.left(360/i) # 360도/60도씩 좌측으로 회전과 동시에 그린다.

#별 만들기 (중간에 허리케인 모양 있음)
for x in range(140): # x를 140번 돌린다

    if x % 3 == 0: # x 를 3으로 나누고 나머지가 0과 같으면 red출력

        t.color("red")

    if x % 3 == 1: # x 를 3으로 나누고 나머지가 1과 같으면 white출력

        t.color("white")

    if x % 3 == 2: # x 를 3으로 나누고 나머지가 2과 같으면 blue출력

        t.color("blue")

    t.forward(x*2)  # if문을 벗어나도 for문은 안 벗어났으니 반복할 내용 들여쓰기 유지 하면서 입력.  

    t.left(164) #왼쪽 164도 회전

t.mainloop() # 창 그대로 있는것.