class parent:
    x=10
    y=20
    
    @classmethod
    def disData(self):  
        print("parent method")
        print(self.x)
        print(self.y)         

class child(parent):
    x=30
    y=40
    @classmethod
    def disData(self):  
        print("child method")
        print(self.x)
        print(self.y) 
        super().disData()

obj=child()
obj.disData()


