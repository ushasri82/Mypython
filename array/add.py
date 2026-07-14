from array import *
array1=array('i',[10,20,30,40,50])
array2=array('i',[60,70,80,90,100])

#adding append,insert,extend
array1.append(60)
print("After append:", array1)
array1.insert(2,25)
print("After insert:", array1)
array1.extend(array2)
print("After extend:", array1)