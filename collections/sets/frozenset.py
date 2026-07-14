#frozen set
#creating a frozenset
my_frozenset = frozenset([1, 2, 3, 4, 5])
print("Frozenset:", my_frozenset)
#accessing the frozenset
print("Accessing the frozenset:")
for item in my_frozenset:
    print(item)
#checking if an item is in the frozenset
print("Is 3 in the frozenset?", 3 in my_frozenset)
print("Is 6 in the frozenset?", 6 in my_frozenset)
#checking the item is not in the frozenset
print("Is 6 not in the frozenset?", 6 not in my_frozenset)
#length of the frozenset
print("Length of the frozenset:", len(my_frozenset))