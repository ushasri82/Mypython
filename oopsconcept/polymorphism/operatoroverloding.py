class student:
    def __init__(self,marks):
        self.marks=marks
    def __add__(self,other):
        return self.marks+other.marks
student1=student(50)
student2=student(60)
print(student1+student2)


#subtraction
class student:
    def __init__(self,marks):
        self.marks=marks
    def __sub__(self,other):
        return self.marks-other.marks
s1=student(50)
s2=student(30)
print(s1-s2)
class Employee:
    def __init__(self, name, salary, bonus):
        self.name = name
        self.salary = salary
        self.bonus = bonus

    def __add__(self, other):
        return self.salary + other.salary

    def __gt__(self, other):
        return self.bonus > other.bonus

    def __str__(self):
        return self.name + " " + str(self.salary) + " " + str(self.bonus)


e1 = Employee("Sai", 10000, 2000)
e2 = Employee("Kiran", 20000, 3000)

print(e1)
print(e2)

print("Combined Salary =", e1 + e2)

if e1 > e2:
    print("Higher Bonus:", e1)
else:
    print("Higher Bonus:", e2)
 