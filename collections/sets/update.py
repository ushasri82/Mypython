#update the sets
my_set = {1, 2, 3, 4, 5}
print("Original Set:", my_set)
#updating the set with another set
another_set = {6, 7, 8}
my_set.update(another_set)
print("Set after updating with another set:", my_set)
#updating the set with a list
my_list = [9, 10]
my_set.update(my_list)
print("Set after updating with a list:", my_set)
#updating the set with a tuple
my_tuple = (11, 12)
my_set.update(my_tuple)
print("Set after updating with a tuple:", my_set)
#updating the set with a string
my_string = "hello"
my_set.update(my_string)
print("Set after updating with a string:", my_set)

#joining the sets
set1 = {1, 2, 3}
set2 = {4, 5, 6}
joined_set = set1.union(set2)
print("Joined Set:", joined_set)

#loop through the set
print("Looping through the set:")
for item in my_set:
    print(item)
    
