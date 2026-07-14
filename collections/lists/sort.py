#copying ,sorting and looping through list
my_list = [5, 2, 9, 1, 5, 6]
#copying a list
copied_list = my_list.copy()
print("Original List:", my_list)
print("Copied List:", copied_list)
#sorting a list
sorted_list = sorted(my_list)
print("Sorted List:", sorted_list)
#looping through a list
print("Looping through the list:")
for item in my_list:
    print(item)
    
#list comprehension
squared_list = [x**2 for x in my_list]
print("Squared List:", squared_list)
