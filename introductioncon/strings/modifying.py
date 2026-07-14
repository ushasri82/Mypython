s1="ushasri"
print ("original string:", s1)
l1=list(s1)

l1.insert(4,"great")

print (l1)

s1=''.join(l1)
print ("Modified string:", s1)