class cloth:
    price=200
    @classmethod
    def showprice(cls):
        return cls.price
        
c=cloth()
print(c.showprice())


#class method anorher type (converting the instance method into the class method)
class student:
    stdcount=0
    def __init__(self,age,branch):
        self.age=age
        self.branch=branch
        student.stdcount+=1
    def showcount(self):
        print(self.stdcount)
    counter=classmethod(showcount)
s1=student(21,"cse")
s2=student(22,"ece")
    
s1.showcount()
student.counter()        