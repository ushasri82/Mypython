#removing the elments from te sets
my_set = {1, 2, 3, 4, 5}
print("Original Set:", my_set)
#removing an element using remove()
my_set.remove(3)
print("Set after removing 3:", my_set)
#removing an element using discard()
my_set.discard(4)
print("Set after discarding 4:", my_set)

#set comprehesion
squared_set = {x**2 for x in my_set}
print("Squared Set:", squared_set)

