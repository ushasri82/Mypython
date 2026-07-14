from array import *
array1=array('i',[18,5,20,55,33,6])
#sorting the array using the sorting algorithm
for i in range(len(array1)):
    for j in range(i+1, len(array1)):
        if array1[i] > array1[j]:
            temp=array1[i]
            array1[i]=array1[j]
            array1[j]=temp
print("Sorted array:", array1)

#sorting the array using the sort() method
array2=array1.tolist()
array2.sort()
a=array('i', array2)
print("Sorted array:", a)

#sorting the array using the sorted() method
array2=sorted(array1)
a=array('i', array2)
print("Sorted array:", a)
