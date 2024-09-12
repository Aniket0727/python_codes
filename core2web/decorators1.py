# def outerFunc():
#     print("In outer fun")
    
#     def innerFun1():
#         print("In inner fun-1")
        
#     def innerFun2():
#         print("In inner fun-2")

#     return innerFun1,innerFun2

    
# a=outerFunc()
# a[0]()
# a[1]()

def  isPalindrome(fun):
    def wrapper(*args,**kwargs):
        result=fun(*args,**kwargs)
        if isinstance(result,str)and result==result[::-1]:
            return "String is [palin]"
        else:
            return "not"
    return wrapper

@isPalindrome
def palindrome(s):
    return s
print(palindrome("radeer"))