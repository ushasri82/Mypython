class animal:
    def display(self):
        print("animals")
class dog(animal):
    def show(self):
        print("dog is animal")
class puppy(dog):
    def eating(self):
        print("puppy is eating")
p=puppy()
p.eating()
p.show()
p.display()
    
    
    
    
    
    
    
    
# Base class
class Vehicle:
    def start(self):
        return "Vehicle starts"

# Derived class
class Car(Vehicle):
    def start(self):
        return "Car starts"
        super().start()

# Sub-derived class
class SportsCar(Car):
    def start(self):
        return "Sports Car starts"

# Creating an instance of SportsCar
sports_car = SportsCar()
print(sports_car.start())  

s=Car()
print(s.start())


