# 세로읽기

n = 5
m = []

for i in range(n):
    num = input()
    m.append(num)

for i in range(15):
    for j in range(5):
        if len(m[j]) <= i:
            pass
        else:
            print((m[j])[i], end='')
