class student:
    pass
    def __init__(self,name,age):
      self.name=name
      self.age=age
s1=student("usha",21)
print("name:{}".format(s1.name))
print("age:{}".format(s1.age))


#default constructors
class student:
    pass
    def __init__(self,name,age):
        self.name="usha"
        self.age=21
s1=student("navya",8)
print("name:{}".format(s1.name))
print("age:{}".format(s1.age))



#parameterized constructor
class student:
    pass
    def __init__(self,name,age):
        self.name=name
        self.age=age
s1=student("usha",21)
print("name:{}".format(s1.name))
print("age:{}".format(s1.age))
