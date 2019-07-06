#



def get_cubes(n):
    return n**3

l2 = [1,2,3,4,5,6,7]
l1 = list(map(get_cubes,l2))

print(l1)