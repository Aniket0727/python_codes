# class parent1:
    
#     def __init__(self):
#         print("In constructor:parent1")
        
#     def disData(self):
#         print("In disData")

# class parent2:
    
#     def __init__(self):
#         print("In constructor:parent2")
        
#     def printData(self):
#         print("In printData")
        
# class child(parent1,parent2):
#     pass

# obj=child()
# obj.disData()
# obj.printData()



class parent1:
    
    def __init__(self):
        print("In constructor:parent1")
        
    def disData(self):
        print("In disData")

class parent2:
    
    def printData(self):
        print("In printData")
        
class child(parent1,parent2):
    pass

obj=child()
obj.disData()
obj.printData()





