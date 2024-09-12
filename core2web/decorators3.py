def decorFun(func):
    
    def wrapper():
        print("Strat Wrapper")
        func()
        print("End Wrapper")
        
    return wrapper

def normalFun():
    print("Normal Function")
    
ret=decorFun(normalFun)
ret()