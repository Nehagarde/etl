#python function don't support function overloading
#this is because of the facility to provide arguments and keyword agrguments



#nonkeyword/compulsory/non-default arguments

def myfunc(a,b,c=10,d=30):
    print("{} {} {} {}" . format(a,b,c,d))

def func1(a,b,c,d=4,e=5,f=6):
    return a+b+c+d+e+f

def func2(*args,**kwargs):
    print(args)
    print(kwargs)

if __name__== '__main__':
    myfunc(1,2)
    myfunc(1,2,3,4)
    myfunc(1,12,d="400",c="800")
    myfunc(c=100,d=300,b=20,a=30)
    # myfunc(c=50,d=60,10,70) error

    t = (1,2,3)
    d={'d':400,'e':500,'g':60000}

    result=func2(*t,**d)

    print(result)

    func2(1,2,3,d=4,e=5,f=6,g=5,l=6)
    s="neha garde"
    print(s.find('a'))
    print(s.index('a'))


    #migrations are python modules which tells django how to create tables by default