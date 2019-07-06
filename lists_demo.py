#list functions


#remove element using remove
ls = [10,20,30,40,50,60,70,80,90,100]
print(ls)
ls.remove(20)
print(ls)

print(dir(ls))

del ls[0]

print(ls)

print(ls.pop()) #removes last element

print(ls.pop(4)) #removes element at given index

print(ls)

ls.append(1000)     #adds element at last

print(ls)

ls.insert(3,500)    #adds element at given index

print(ls)

print(ls.index(80))   #finding index of given element
#print(ls.index(5))

print(ls.insert(ls.index(80),900)) #adding element at given index fetched from ls.index method
print(ls)

print(ls.count(50)) #count of given element

ls.insert(100,700)
print(ls)
#print(ls[100]) #index error
#print(ls[99])


l1 = [20,30,40]
l2 = [60,70,80]

l1.extend(l2)
ls.extend(l1)

print(ls)
ls.append(l1)

print(ls)
# gives error ls.extend(l1).extend(l2)

print(ls)

#copy
l1 = ls.copy()  #two different objects

print(l1)

print(id(ls))
print(id(l1))

print(l2)
l2.reverse()
print(l2)

l4 = [20,30,40,70]
#sort descending
l4.sort(reverse=True)
print(l4)

l4.sort()
print(l4)

print(ls)
print(ls.pop())
ls.sort(reverse=True)
print(ls)

ls.append('y')
ls.sort(reverse=True)
print(ls)
l4.clear()
print(l4)