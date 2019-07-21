""" Purpose
1>>Pre-Processing
2>>Post-Processing


decorator is a function which executes before calling the main function


"""

def mydecorator(funcname):
    print("Hi in decorator")
    def inner(*args,**kwargs):

        print("Preprocessing")

        result = funcname(*args,**kwargs)

        print("Post processing")
        if result<=100:
            return result
        else:
            return 100

    return inner


@mydecorator
def myfunction(a,b,c,d=200):
    print("In my function")
    return a+b+c+d

if __name__ == '__main__':
    print("In main")
    print(myfunction(10,20,30,5))








