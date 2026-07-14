#joining the list
list1 = [1, 2, 3]
list2 = [4, 5, 6]
#using + operator
joined_list = list1 + list2
print(joined_list)
#using extend() method
list1.extend(list2)
print(list1)

#list methods
my_list = [1, 2, 3, 4, 5]
#append() method
my_list.append(6)
print(my_list)
#extend() method
my_list.extend([7, 8, 9])
print(my_list)
#insert() method
my_list.insert(0, 0)
print(my_list)
#concatenation
concatenated_list = my_list + [10, 11, 12]
print(concatenated_list)
#count method
count_3 = my_list.count(3)
print("Count of 3 in the list:", count_3)
#reverse method
my_list.reverse()
print("Reversed List:", my_list)
