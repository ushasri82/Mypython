class animal:
    def display(self):
        print("parent method")
class flower:
    def show(self):
        print("parent method 2")
        
class child(flower,animal):
    def childmethod(self):
        print("child class")
class child2(child):
     def childmethod2(self):
         print("inherited from child method which is inherited from flower parent class")
c=child2()
c.childmethod2()
c.childmethod()
c.show()
c.display()