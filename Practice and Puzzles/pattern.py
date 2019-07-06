

l1=[1,4,5,8,9]

l2= [(i**2) for i in l1]

print(l2)

l1=[]
i=0
while i<len(l2):
    l1.append(l2[i]**2)
    i+=1

print(l1)


for i in range(1,9):
    for j in range(1,i):
        print(j,end="")
    print(end="\n")

s=""
ls=['1','2','3','4','5','6','7','8']
print(ls[0:1])

str=''
for i,v in enumerate(ls):
    str=(s.join(ls[0:i+1]))
    print(str)
for i,v in enumerate(ls):
    str=(s.join(ls[0:i+1]))
    print(str)


