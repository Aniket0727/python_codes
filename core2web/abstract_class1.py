from abc import *

class Demo(ABC):
    def __init__(self):
        print("Const Demo")
    
    @abstractmethod
    def fun(self):
        pass

print(type(ABC))
print(ABC.__base__)
# obj=Demo()
# obj.fun()