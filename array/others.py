"""#Find the sum of all elements in an array.
from array import *
a=array('i',[1,2,3,4,5])
sum=0
for i in a:
    sum+=i
print(sum) """


"""a=[1,2,3,4,5]
print(max(a))
print(min(a))"""

#rotate an array by one position to the right
a=[1,2,3,4,5]
a=a[-1:]+a[:-1]
print(a)

#rotate an array by one position to the left
a=[1,2,3,4,5]
a=a[1:]+a[:1]
print(a)
