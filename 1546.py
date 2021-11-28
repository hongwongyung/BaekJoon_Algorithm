num = int(input())

a = list(map(int, input().split(' ')))
b = max(a)
c = []
d = 0

for i in range((num)):
    answer = a[i] / b * 100
    d += answer
print(d / len(a))