class first:
    
    def __init__(self,a1,name1 ):
        self.a=a1
        self.name=name1
        
    def info(self):
        print(self.a)
        print(self.name)
        
f1=first(10,"Java")
f2=first(20,"Python")    

f1.info()
f2.info()

print(f1.name)
print(f2.a)





