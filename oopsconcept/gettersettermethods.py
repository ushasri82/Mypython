class student:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def set_name(self,name):
        self.__name=name
    def set_age(self,age):
        self.__age=age
        
s=student("usha",21)
print("name:",s.get_name(),"age:",s.get_age())
s.set_name("mohan")
s.set_age(25)
#print("name:",s.get.__name(),"age:",s.get.__age())
print("name:", s.get_name(), "age:", s.get_age())