from array import *
array1=array('i',[10,20,30,40,50])

#copying the array using assignment operator
array2=array1
print("Array1:", array1)
print("Array2:", array2)
print("Array1 id:", id(array1))
print("Array2 id:", id(array2))

#copying the array using deepcopy() method
import copy
array3=copy.deepcopy(array1)
print("Array1:", array1)
print("Array3:", array3)
print("Array1 id:", id(array1))
print("Array3 id:", id(array3))
