class first:
    s="sin"
    
    def __init__(self,a1,name1 ):
        self.a=a1
        self.name=name1
        print(name1)
        
    def info(self):
        print(self.a)
        print(self.name)
        print(self.s)
        print(first.s)
        
        
        
f1=first(10,"Java")

f1.info()
first.info()
