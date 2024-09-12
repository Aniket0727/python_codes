    
# def fun():
#     pass
    
# print(type(fun))


class function:

    def __new__(self):
        print("new: ",self)
        return super().__new__(self)
        
            
    def __init__(a):
        print("init: " ,a)
        
        

f=function()

