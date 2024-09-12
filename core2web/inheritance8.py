class Demo:
    
    def __init__(self):
        print("In const")
        
    def __del__(self):
        print("In des")
        
def fun():
    print("In fun")
    obj=Demo()
    print("End Fun")
    
fun()
print("End Code")