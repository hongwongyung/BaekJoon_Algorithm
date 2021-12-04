x = int(input())
average = []
answer = []

for i in range(x):
    y = 0
    a = list(map(int, input().split(' ')))
    for j in range(1, a[0]+1):
        y += a[j]
    average = y / a[0]
    people = 0
    for z in range(1, a[0]+1):
        if a[z] > average:
            people += 1
    q = 100*(people/a[0])
    if people == 0:
        answer.append(('%.3f' % 0))
    else:
        answer.append(('%.3f' % q))

answer_str = list(map(str, answer))

for j in (answer_str):
    print(j + '%')