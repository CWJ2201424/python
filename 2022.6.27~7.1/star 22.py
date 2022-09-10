
n = 5
line = n * 2 - 1
star="*"
space=' '

for i in range(n, 0, -1):
    if i == n:
        print(space * (line//2), end='')
        print(star)
    elif i == 1:
        print(star * line)
    else:
        print(space * (i - 1) + star, end='')
        print(space * (line - i * 2) + star)
