def gun():
    print("gun")
    
def run(y):
    print("Run")
    y()

def fun(x):
    print("Fun")
    x()
    
    
fun(run(gun))