class type:
    
    def __init__(self,x):
        print("self")
        # print(self)
        print()
        # print(x)


class Demo(object):
    
    def __init__(self):
        self.x=10
        super().__init__()
         
class Demochild(Demo):
    def __init__(self):
        
        self.y=20
        super().__init__()
        
    def printData(self):
        
        print(self.x)
        print(self.y)

obj=Demochild()
obj.printData()        
print()    
type(obj)
        

