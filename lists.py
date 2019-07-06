#creating lists

l=[10,20,30,40,50,60,70,80,90]

#lists can contain duplicates

l=[10,10,20,30,40,50,60,70,80,90]

print(dir(l))

print(l[5])
#positive index

#negative index

# slice
#ls[start_index:end_index:step_counter]


print(l[-5:-2])


#string/list reverse
print(l[::-1])

# Adding only required key,values using fromkeys



dict = {'a':10, 'b':20, 'c':30}
ls = ['a','b','c','d','e','f','g']

new_dict = dict.fromkeys([i for i in ls if i not in dict.keys()],50)

print(new_dict)
dict.update(new_dict)
print(dict)


print("Reverse split")
print(l[-2:-5:-1])

print("Check if palindrome")

if l == l[::-1]:
    print(l)
    print("Palindrome")
else:
    print(l[::-1])
    print("Not a palindrome")




#Test


if __name__ == '__main__':
    l1 = eval(input("Enter list:"))
    l2=[]

    for item in l1:
        l2.append(item**3)

    print(l2)

    x1 = [1,2,3,4]
    x2 = [5,6,7]

    print(id(x1))
    print(id(x2))
    x1 = x1+x2
    print(x1)
    print(id(x1))

    x1 = [1, 2, 3, 4]
    x2 = [5, 6, 7]

    print(id(x1))
    print(id(x2))
    x1 += x2
    print(x1)
    print(id(x1))

