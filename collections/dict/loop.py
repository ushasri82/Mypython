mydict={"1":"usha","2":"sri","3":"is studying","4":"final year"}
for i in  mydict:
    print(i)

for i in mydict.values():
    print(i)
    
for index,key in enumerate(mydict):
        print(index,key)

for index,(key,value) in enumerate(mydict.items()):
    print(index,key,value)
    
    
