x = int(input())
index = 1001
a=[]

for i in range(index):
    for j in range(index):
        if x == 3*i + 5*j:
            a.append(i+j)
if len(a) > 0:
    print(a[0])
else:
    print(-1)