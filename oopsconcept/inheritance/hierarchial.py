class animal:
    def display(self):
        print("animal")
        
class dog(animal):
    def show(self):
        print("cat is an animal")
class cat(animal):
    def show1(self):
        print("cat is animal too")
c=cat()
c.display()
c.show1()
d=dog()
d.display()
d.show()