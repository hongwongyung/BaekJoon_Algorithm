def add(a,b):
    if (b>=45):
        a = a
        b = b-45
        print(a,b)

    elif(a<=0 and b>=45):
        a = a+23
        b = b-45
        print(a,b)

    elif(a<=0 and b<45):
        a = a+23
        b = b+15
        print(a,b)

    else:
        a = a-1
        b = b+15
        print(a,b)
        

a,b = map(int, input().split())
c = add(a,b)
print = (c)