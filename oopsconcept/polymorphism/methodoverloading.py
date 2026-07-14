class demo:
    def add(self,*args):
        return sum(args)
d=demo()
print(d.add(1,2))
print(d.add(1,2,3,4,5))


class demo:
    def add(self,*args):
        if len(args)==2:
            return args[0]+args[1]
        elif len(args)==3:
            return args[0]+args[1]+args[2]
d=demo()
print(d.add(1,2))
print(d.add(1,2,3))


#implementing methodoverloading using multipledispatch
from multipledispatch import dispatch
class demo:
    @dispatch(int,int)
    def add(self,a,b):
        x= a+b
        return x
    @dispatch(int,int,int)
    def add(self,a,b,c):
        x= a+b+c
        return x
d=demo()
print(d.add(1,2))
print(d.add(1,2,3))