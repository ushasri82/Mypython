#add the iemas to dict
mydict={"1":"usha","2":"sri"}
mydict['3']="studying python"
mydict["4"]="enthusiatically"
print(mydict)

#removing items in dict
mydict.pop("4")
print(mydict)
mydict.popitem()
print(mydict)

del mydict["1"]
print(mydict)

mydict.clear()
print(mydict)
