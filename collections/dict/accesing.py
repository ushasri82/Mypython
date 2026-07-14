#dictionary
mydict={"1":"hello","2":"hii","3":"world"}
print(mydict)
#accessing the items in dict
print(mydict["2"])
print(mydict.get("1"))
print(mydict.values())

#changing the values
mydict["2"]="hello..."
print(mydict)

#update the dict
mydict2={"4":"usha","5":"sri"}
mydict.update(mydict2)
print(mydict)
