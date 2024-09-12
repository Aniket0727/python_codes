class first:
    
    def __init__(self):
        print("init")
        self.a=10
        self.name="python"
        
    def info(self):
        print("fun")
        print(self.a)
        print(self.name)
        
f1=first()
f2=first()    
print(f1)
print(f2)

# f1.info()