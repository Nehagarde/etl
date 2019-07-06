#tuples, strings and numbers are immutable

t = (1,23,4)

print(dir(t))

print(t.count(23))

print(t.index(4))

t1 = (1,2,3)
t2 = (2,3,4)
print(id(t1))
print(id(t2))

t1 = t1+t2
print(id(t1))

l = [1,2,3]
t  = (10,20,30,l)

print(t)

l.append(20)

print(t)

dict1 = {(1,2,3):'This is a dict with tuple as key'}
#you cannot add mutable objects in a dictionary key
print(dict1)


#replace strings 3rd argument tells the number of found strings to be replaced
s="vikas,gulab,jamdar"
s1= s.replace("vikas","v",2)

s2 = "how are you how are you you you you"
s3=s2.replace("you","y",2)
print(s3)

#since strings are immutable if content is exactly the same the it refers to the same object
t1="neha"
t2="neha"

print(id(t1))
print(id(t2))

if t1 is t2:
    print("Same objects")

#lists
l1=[10,10,20]
l2=[10,10,20]

print(id(l1))
print(id(l2))

if l1 is l2:
    print("Same objects")

if l1 == l2:
    print("Contents are same but different objects")

#integers
i1=1234
i2=1234

print(id(i1))
print(id(i2))

if i1 is i2:
    print("Same objects")

if i1 == i2:
    print("Contents are same and so are objects")


a = 10
b = 12.5
c = "neha"

print("%d %s %f" % (a,c,b))
print("{} {} {}".format(a,b,c))


t = (1,2,3)
c = t
print(c)