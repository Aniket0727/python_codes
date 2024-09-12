# #operator overloading

class Demo:
    x=10
    
class Memo:
    def __eq__(self,obj):
        print("hi")
        x=20
        return id(self)==id(obj)
        

obj1=Demo()
obj2=Memo()

print(obj1==obj2)
# print(id(obj1))
# print(id(obj2))

x=20
y=10.5
print(x+y)
