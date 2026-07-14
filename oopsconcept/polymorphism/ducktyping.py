class dog:
    def speak(self):
        print("bark")
class cat:
    def speak(self):
        print("meow")
def makesound(animal):
    animal.speak()
makesound(cat())
makesound(dog())
    
        
    
    
class dog:
    def speak(self):
        return "bark"
class cat:
    def speak(self):
        return "meow"
def makesound(animal):
    animal.speak()

c=cat()
d=dog()
makesound(c)
makesound(d)