# String Methods in Python  

a = "welcome to python programming"

print("Original String:", a)
print()

# Case conversion methods
print("UPPERCASE:", a.upper())
print("lowercase:", a.lower())
print("swapcase:", a.swapcase())
print("Capitalized:", a.capitalize())
print("Title Case:", a.title())

print()

# Useful string checks
print("Is all lowercase?:", a.islower())
print("Is all uppercase?:", a.isupper())
print("Is alphabetic?:", a.isalpha())
print("Is alphanumeric?:", a.isalnum())

print()

# String operations
print("Length of string:", len(a))
print("Count of 'o':", a.count("o"))
print("Find position of 'python':", a.find("python"))

print()

# Replacement and splitting
print("Replace 'python' with 'Java':", a.replace("python", "Java"))
print("Split words:", a.split())

print()

# Strip (useful for removing spaces)
b = "   hello python   "
print("Original with spaces:", b)
print("Stripped:", b.strip())