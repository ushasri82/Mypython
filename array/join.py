from array import *
a=array('i',[10,20,30])
b=array('i',[40,50,60])

#joining the two arrays using the append method
for i in range(len(b)):
    a.append(b[i])

print("Joined array:", a)

#joining the two arrays using the + operator
x=a.tolist()
y=b.tolist()
z=x+y
c=array('i', z)
print("Joined array:", c)

#joining the two arrays using the extend() method
a.extend(b)
print("Joined array:", a)