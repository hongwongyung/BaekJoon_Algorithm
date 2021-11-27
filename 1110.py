input = (input())
int_list_input = list(map(int, input))
num = 0

if len(int_list_input) == 1:
    (int_list_input.append(0))
    list(map(int, int_list_input))
    answer = (str(int_list_input[0])+str(int_list_input[1]))
else:
    answer = input

while True:
    i = str(int_list_input[0] + int_list_input[1])
    str_list_input = list(map(str, int_list_input))
    y = str(i[-1])
    int_list_input = (str_list_input[1] + y)
    num = num + 1
    if int_list_input == answer:
        print(num)
        break
    else:
        int_list_input = list(map(int, int_list_input))
