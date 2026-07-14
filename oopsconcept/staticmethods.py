class student:
    stdcount = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        student.stdcount += 1

    def showcount():
        return student.stdcount

    count = staticmethod(showcount)

s1 = student("ramu", 21)
s2 = student("ramu", 23)

print(student.count())
    
    