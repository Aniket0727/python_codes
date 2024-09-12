class Demo:
    
    def __init__(self):
        self.x=10  
        self._y=20  
        self.__z=30

    def __fun(self):
        print("In Fun")
        

obj=Demo()
obj._Demo__fun()
print(obj.x)
print(obj._y)
print(obj._Demo__z)

        