def decorFun(func):                             #3
    print("In decor fun")                       #4
    # print(func)       #addres of normalFun
    def wrapper(*args):                         #6
        print("Strat Wrapper")                  #7
        val=func(*args)                         #8
        # print(args)     #10,20 in args
        print("End Wrapper")                    #12
        return val                              #13
    return wrapper                               #5

@decorFun                                        #2
def normalFun(x,y):                              #9
    print("Normal Function")                    #10
    return x+y                                  #11
    
# normalFun=decorFun(normalFun)
print(normalFun(10,20))                           #1  ---#14

