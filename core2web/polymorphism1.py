# class Demo:
#     def fun(self):
#         print("In Demo: fun")
        
# class Memo:
#     def fun(self):
#         print("In Memo: fun")
        
# def callFun(obj):
#     obj.fun()
    
# obj1=Demo()
# obj2=Memo()

# callFun(obj1)
# callFun(obj2)
# #

class Demo:
    def fun(self):
        print("In Demo: fun")
        
class Memo:
    def fun(self):
        print("In Memo: fun")
        
def callFun(obj):
    if hasattr(obj,'fun'):
        obj.fun()
    elif hasattr(obj,'gun'):
        obj.gun()
        
obj1=Demo()
obj2=Memo()
# callFun(obj1)
callFun(obj2)

# if hasattr(obj1,'fun'):
#     print('yes')


