from abc import ABCMeta,abstractmethod

class department(metaclass=ABCMeta):
    
    def slogan(self):
        print("Student power")
        
    @abstractmethod
    def CSE(self):
        pass
    
class college(department):

    def CSE(self):
        pass

class university(college):

    def CSE(self):
        print("CSE")
        
# print(type(department))
# print(type(college))
# print(type(university))

obj=college()
obj.CSE()
obj.slogan()
obj1=university()
obj1.CSE()
print(obj1.CSE())

obj1.slogan()