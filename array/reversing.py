from array import *
array1=array('i',[10,20,30,40,50])

#reversing the array using the slicing operation
array2=array1[::-1]
print("Original array:", array1)
print("Reversed array:", array2)

#reversing the array using the reverse() method
array2=array1.tolist()
array2.reverse()
print("Original array:", array1)
c=array('i', array2)
print("Reversed array:", c)

#reversing the array using the reversed() method
array2=reversed(array1)
print("Original array:", array1)
c=array('i', array2)
print("Reversed array:", c)


#reversing the array using the for loop
array2=[]
for i in range(len(array1)-1, -1, -1):
    array2.append(array1[i])
print("Original array:", array1)
print("Reversed array:", array2)