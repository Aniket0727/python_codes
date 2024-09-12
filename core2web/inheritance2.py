class Company(object):
    x=10
    
    def __init__(self,compName,loc):
        print("In constructure")
        self.compName=compName
        self.loc=loc
     
    def compInfo(self):
        print(self.compName)
        print(self.loc)

class Employee(Company):
    pass        
obj1=Employee("mic","pune")
obj2=Employee("mic","beed")

obj1.compInfo()
obj2.compInfo()
