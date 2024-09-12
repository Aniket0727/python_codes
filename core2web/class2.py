class first:
    
    def __init__(self):
        print("init")
        
    def __new__(cls):
        print("new")
        
        
first()

