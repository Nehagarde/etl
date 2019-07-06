#list comprehension
l = [2,2,3,4,5,6,6,7,8,8,9]
def list_comprehension(l):
    return [item for item in l if l.count(item)==1]

print(len(l))



#dictionary comprehension:
def dict_comprehension(l):
    return {k:k**3 for k in l}

l2 = [
    [1,2,3],[4,5,6]
]

l3 = []
for l1 in l2:
    for item in l1:
        l3.append(item)

print(l3)


l4 = [item for l1 in l2 for item in l1]

print(l4)

if __name__ == '__main__':
    l5 = eval(input("Enter list for list comprehension:"))
    o = list_comprehension(l5)
    print(o)

    l6 = eval(input("Enter list for dict comprehension:"))
    o = dict_comprehension(l6)
    print(o)