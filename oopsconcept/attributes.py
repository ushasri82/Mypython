#class attribute
class student:
    name="usha"
    age=21
s1=student()
print(s1.name)
print(s1.age)


#instance attribute
class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print ("name:",self.name,"age:",self.age)
s1=student("usha",21)
s2=student("jenny",15)  

#combining both
class student:
    name="usha"
    age=21
    def __init__(self,branch,marks):
         self.branch=branch
         self.marks=marks
         print("branch",self.branch,"marks:",self.marks)
s1=student("cse",25)
print("name:",student.name)
print("age:",student.age)      
        