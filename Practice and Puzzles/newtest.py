#list of integers
l1 = [3,4,7,8,9,2,2,4,5,5,1,1,7]

[print("Count of %s is %s" %(item,l1.count(item))) for item in set(l1)]


#if an integer is provided
n = eval(input("Enter integer: "))

l2=[]

while n:
    rem=n%10
    l2.append(rem)
    n=n//10

l2.reverse()
[print("Count of %s is %s" %(item,l2.count(item))) for item in set(l2)]

