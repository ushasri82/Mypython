#sets
my_set = {1, 2, 3, 4, 5}
print(my_set)
#accessing the set
print("Accessing the set:")
for item in my_set:
    print(item)
#checking if an item is in the set
print("Is 3 in the set?", 3 in my_set)
print("Is 6 in the set?", 6 in my_set)
#checking the item is not in the set
print("Is 6 not in the set?", 6 not in my_set)
#lenthn oif the ste
print("Length of the set:", len(my_set))
#adding an item to the set
my_set.add(6)
print("Set after adding 6:", my_set)
