from functools import reduce

def sum(a,b):
    return a+b

l1 = [1,2,3,4,5,6,7,8,9,0]
res = reduce(sum,l1)
re1 = range(20,30)
print(res)
print(reduce(sum,re1))