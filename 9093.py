n = int(input())

for i in range(n):
        a = input()+" "
        arr = []
        for j in a:
            if j !=" ":
                arr.append(j)
            else:
                while arr:
                    print(arr.pop(), end='')
                print(' ', end='')