import sys
input = sys.stdin.readline

n = int(input())
stack = []

for i in range(n):
    stk = input().split()
    if stk[0] == 'push':
        stack.append(int(stk[1]))
    elif stk[0] == 'top':
        if len(stack) > 0:
           print(stack[-1])
        else: print(-1)
    elif stk[0] == 'pop':
        if len(stack) > 0:
           print(stack.pop())
        else: print(-1)
    elif stk[0] == 'size':
        print(len(stack))
    elif stk[0] == 'empty':
        if len(stack) > 0:
           print(0)
        else: print(1)