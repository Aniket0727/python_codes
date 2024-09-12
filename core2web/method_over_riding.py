#Method overloading

# Method overriding occurs when a subclass provides a specific implementation
# for a method that is already defined in its superclass. This allows the subclass
# to customize the behavior of the method while still retaining the method signature 
# (name and parameters) from the superclass.


class Parent:
    def fun(self):
        print("fun:parent")
        
    def gun(self):
        print("gun:parent")

class Child(Parent):
        
    def gun(self):
        print("gun:Child")
        return 10

obj1=Child()
obj1.fun()
obj1.gun()
