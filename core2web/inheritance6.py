def fun():
    print("Fun")

class Demo:
    fun()

    def fun2():
        print("fun2")
    fun2()
    
    print("Start class ")
    
    def __init__(self):
        print("In init")
        
    print("end class")

print("start code")
obj=Demo()
print("End code")