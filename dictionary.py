d = {}
di = dict()
print(di)   #returns emoty list
d = {'a':20,'b':30}

d['c']=40
d['a']=50
print(d['a']) #if key does not exists it gives error
del d['a']

print(dir(d)) #namespace for corresponding object

print(d.get('c')) #get allows you to get the value of a given key
print(d.get('h'))

d['e']=50
print(d.get('h',100)) # to handle keyError we can give a default value
d['f']=60
#pop returns the value which of the selected element
print(d.pop('f'))

d['f']=60
print(d.get('f'))
print("======================================================")
print(d.get('f',200))

#all functions have small letters
d.setdefault('m',200)
d.setdefault('f',200) #assigning new key value pair
#if existing key is present it gives the existing value

print(d.get('f'))
print(d.get('m'))

d['z'] = 500
t = d.popitem() #gives the key value pair of the popped item
print(t)

print('*'*3)
for tuple in d.popitem():
    print(tuple)

print('*'*3)
d['a']=50
d['b']=60
d['c']=70
d['x']=80
d['t']=90

print(d.keys())
for i in d.keys():
    print(i)

for i in d.values():
    print(i)

print(d.values())
print('*'*5)
for k in d:
    print(k)

print(d.items())

for k,v in d.items():
    print(k)
    print(v)


temp = d.copy()
print(temp)
d2={}
d2['m']=20
d2['l']=30
d2['b']=70
d.update(d2)

print(d)

print(dir(d))

#from keys is used to assign a common value to multiple keys
print('00000'*5)
print(d)
d.update(d.fromkeys(['q','w','r','a','b'],60))


print(d)
print('00000'*5)

d2.clear()
print(d2)

