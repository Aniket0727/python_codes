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
class child(parent):
    pass

obj=parent()
obj.disData()
obj.disParent()
