def decorFun(func):             #6    decorRun -wrapper address
    
    def wrapper():              #9
        print("Start Wrapper2")  #10
        func()                  #11
        print("End Wrapper2")   #12
        
    return wrapper               # 7    

def decorRun(func):              #3    func-normal fun address
    
    def wrapper():               #12
        print("Start Wrapper1")  #13
        func()                   #14
        print("End Wrapper1")    #16
        
    return wrapper              #4

@decorFun                       #5
@decorRun                       #2    
def normalFun():
    print("In normal Fun")      #15
    
# normalFun=decorFun(decorRun(normalFun))    
normalFun()                                 #1   #8  #18