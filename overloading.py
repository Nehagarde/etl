class MyClass:

    def myfunc(self,a):
        print("Executing 1st function")

    def myfunc(self,a,b):
        print("Executing 2 function")

    def myfunc(self):
        print("Executing 3 function")


class MyOverload:
    def __init__(self,a):
        self.a = a

    def __add__(self, other):
        return self.a + other.a

    def __mul__(self, other):
        return self.a * other.a

    def __eq__(self, other):
        return self.a == other.a

    def __neq__(self, other):
        return self.a != other.a

if __name__ == '__main__':
    obj = MyClass()
    obj.myfunc()

    obj1 = MyOverload(10)
    obj2 = MyOverload(20)

    result = obj1 + obj2

    print("result = == ",result)
    print("__mul__",obj1*obj2)
    print("__eq__",obj1==obj2)
    print("__ne__",obj1!=obj2)

