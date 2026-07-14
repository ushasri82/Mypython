#string formatting in python
name = "usha sri"
age = 21
marks = 90.05

# Old style formatting
print("Name: %s" % name)
print("Age: %d" % age)
print("Marks: %.2f" % marks)

#format() method
print("Name: {}".format(name))
print("Age: {}".format(age))
print("Marks: {:.2f}".format(marks))
print("Student: {} is {} years old".format(name, age))

#f-strings
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Marks: {marks:.2f}")
print(f"Student: {name} is {age} years old")
