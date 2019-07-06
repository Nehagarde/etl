
def fib(num):
    a = 0
    b = 1
    print("{} {}" % format(a,b))
    for i in num:
        c=a+b
        a,b = b,c
    print(c)








if __name__ == '__main__':
    nums = eval(input("Enter the number of elements in series: "))
    fib(nums)




