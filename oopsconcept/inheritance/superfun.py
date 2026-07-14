class parent:
    def display(self):
        print("parent class")
class child(parent):
    def show(self):
        print("child method")
        super().display()
c=child()
c.show()