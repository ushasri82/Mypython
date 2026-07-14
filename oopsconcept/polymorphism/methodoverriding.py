class animal:
    def method(self):
        print("paremt method")
        
class dog(animal):
    def method(self):
        print("child method")
        super().method()
d=dog()
d.method()     