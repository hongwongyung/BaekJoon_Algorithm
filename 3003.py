input = (input().split(' '))
inputs = list(map(int, input))
inputs[0] = 1 - inputs[0]
inputs[1] = 1 - inputs[1]
inputs[2] = 2 - inputs[2]
inputs[3] = 2 - inputs[3]
inputs[4] = 2 - inputs[4]
inputs[5] = 8 - inputs[5]
for i in inputs:
    print(i, end=' ')