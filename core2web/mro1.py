class Ajoba:
    def fun(self):
        print("In fun: Ajoba")
        
class Parent1(Ajoba):
    pass

class Parent2(Ajoba):
    def fun(self):
        print("In fun: Parent2")
        
class Child(Parent1,Parent2):
    pass

obj1=Child()
obj1.fun()
# print(Child.mro())

print(Child.__mro__)

#in mro to give parent in same sequence in ()