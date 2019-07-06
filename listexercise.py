# sort list based on the first element of a list of tuple

#sorting of lists withing tuple
l1 = [(1,30),(4,60),(2,70),(8,90)]

l1.sort(key=lambda x:x[0])

print(l1)



#sorting of lists
l2 = [{'age':20,'name':'neha'},{'age':10,'name':'garde'}]

l2.sort(key=lambda x:x['age'])

print(l2)


