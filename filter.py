#filters

#this accepts 2 parameters
#first param: function object
#second param: iterable


def chek_even(n):
    if n%2 == 0:
        return True
    else:
        return False



l2 = [1,2,3,4,5,6,7]
l1 = list(filter(chek_even,l2))
print(list(l1))
print(l1)

print(list(filter(lambda x:x%2==0,l2)))