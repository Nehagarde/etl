from threading import Thread, current_thread

class MyThread(Thread):
    def __init__(self,*args,**kwargs):
        self.myargs = kwargs["args"]
        Thread.__init__(self,*args,**kwargs)

    def run(self):
        print("self.args====",self.myargs)
        print("Custom thread name===",current_thread().name)
        for number in self.myargs:
            self.getcubes(number)


    def getcubes(self,n):
        for i in range(n):
            print("cube of %d==%d"%(i,i**3))

def function1(n,m):
        for i in range(n):
            print("Executing thread==%s"%current_thread().name)
            print("%d", i)

if __name__=='__main__':
    #t1 = Thread(target=function1,args=(10,20))


    mythread = MyThread(args=(10,20,30),target=function1,name="custom")
    mythread.start()