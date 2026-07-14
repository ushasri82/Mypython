class student:
    def __init__(self,name,marks):
        self.name=name
        self.__marks=marks
    def displaymarks(self):
        print("the marks are",self.__marks)
    
s=student("ushasri",21)
#print(s.__marks)
s.displaymarks()
print(s.name)