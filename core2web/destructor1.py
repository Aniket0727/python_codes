class parent:
    z=30
    def __init__(self):
        print("In constructor parent")
        self.x=10
        self.y=20
    
    def disData(self):
        print(self.x)
        print(self.y)  
        
    @classmethod
    def disParent(cls):  
        print(cls.z)    
    
    def __del__(self):
        print("In destructor")  

obj=parent()
obj.disData()
obj.disParent()
# obj.__del__()
del obj
