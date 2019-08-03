"""Custom Exceptions"""

class MyExcept(Exception):
    def __init__(self):
        print("Calling Exception")

    def __str(self):
        return("This is a custom exception")


if __name__ == '__main__':
    a = MyExcept()
    print(a)

    print("Raising Exception")
    try:
        raise a
        print(1/10)
    except MyExcept as e:
        print("Caught custom exception MyException")
        print(e)
    except Exception as e:
        print("Caught Parent Exception")
        print(e)
    print("Continuing Exception... ")
