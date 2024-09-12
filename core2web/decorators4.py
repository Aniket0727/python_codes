def decorFun(func):
    
    def wrapper():
        print("Strat Wrapper")
        func()
        print("End Wrapper")
        
    return wrapper

@decorFun
def normalFun():
    print("Normal Function")
    
# normalFun=decorFun(normalFun)
normalFun()


# def fun(*args):
#     print(type(args))

# fun(10,20,30,"1")