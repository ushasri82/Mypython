from array import *
array1=array('i',[10,20,30,40,50])
print(array1[0])
print(array1[1])

#accessing the elements of array using iteration method
for i in array1:
    print(i)
    
#accesing the elements of array using the enumerate method
for index, value in enumerate(array1):
    print(f"index: {index}, value: {value}")