class employee:
    def __init__(self,name,age,salary):
        self.name=name
        self.__age=age
        self._salary=salary
    def display(self):
        print("name:",self.name,"age:",self.__age,"salary:",self._salary)
        
s=employee("nani",21,5000)
print(s.name)
print(s._employee__age)
print(s._salary)
