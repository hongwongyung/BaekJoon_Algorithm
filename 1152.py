input = list(map(str, input().split(' ')))

if input[0] == '':
    del input[0]
if input[-1] == '':
    del input[-1]
print(len(input))