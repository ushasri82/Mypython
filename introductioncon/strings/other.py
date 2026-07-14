

"""a="my name is usha sri"

a=a.replace(" ","")
print(a) """
    
#to check the string start with the given string
"""a = "Hello Python"
print(a.startswith("Hello"))
    
#to check the string end with the given string
a = "Hello Python"
print(a.endswith("Python")) """

"""#print charecters of even indices and odd indices
a = "Hello Python"
print(a[::2]) #even indices
print(a[1::2]) #odd indices """

"""#to count vowels in a string
a = "education"

count = 0

for i in a:
    if i in "aeiouAEIOU":
        count += 1

print(count)

#to count the consonsnts in a string
a = "education"
count = 0
for i in a:
    if i not in "aeiouAEIOU":
        count += 1
print(count) """


"""#to count the words in a string
a = "Python is easy to learn"

words = a.split()
print(len(words)) """


"""#to check the string is palindrome or not
a = "madam"

if a == a[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")"""
    
    #to remove the duplicate characters from a string
a = "programming"

result = ""

for i in a:
    if i not in result:
        result += i

print(result)    
    