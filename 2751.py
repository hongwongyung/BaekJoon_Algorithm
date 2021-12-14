N = int(input())
num = []

for i in range(N):
    num.append(int(input()))

num = sorted(set(num))

for i in num:
    print(i)