def call_bubble_sort(ls):
    n = len(ls)
    for i in range(n):
        for j in range(0,n-1-i):

            if ls[j] > ls[j+1]:
                ls[j],ls[j+1] = ls[j+1],ls[j]

    print(ls)

if __name__ == '__main__':
    print(range(4))
    ls = eval(input("Enter list of numbers: "))

    call_bubble_sort(ls)

