input_list = list(eval(input("Enter a list of numbers to be sorted")))


for i in range(0,len(input_list)):
    for j in range(0,len(input_list)-1-i):
        if input_list[j] > input_list[j+1]:
            input_list[j],input_list[j+1] = input_list[j+1],input_list[j]

print(input_list)


