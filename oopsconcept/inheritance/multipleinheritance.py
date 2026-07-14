class parent:
    def parentmethod1(self):
        print("hello world")
class parent2:
    def parentmethod2(self):
        print("hello")
class child(parent,parent2):
    def childmethod(self):
        print("child method")
c=child()
c.childmethod()
c.parentmethod1()
c.parentmethod2()







