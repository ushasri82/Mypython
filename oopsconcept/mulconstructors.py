class student:
    pass
    def __init__(self,*args):
        if len(args)==1:
            self.name=args[0]
        elif len(args)==2:
            self.name=args[0]
            self.age=args[1]
        elif len(args)==3:
            self.name=args[0]
            self.age=args[1]
            self.branch=args[2]
s1=student("ramu")
print("name",s1.name)
s2=student("ravi",21)
print(f"name:{s2.name},age:{s2.age}")
s3=student("ramesh",22,"cse")
print(f"name:{s3.name},age:{s3.age},branch:{s3.branch}")