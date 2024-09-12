def fun():
    print("start fun")
    yield 10
    yield 100
    yield 1000
    print("end fun")

print(type(fun))     #class 'function'   fkt nava varun tharvt ahe 
print(type(fun()))  #class 'generator'   function call houn return yet ahe manun generator 

for i in fun():
    print(i)


a=fun()
print(type(a))
print(type(fun))

# print(next(a))
# print(next(a))
# print(type(a))
    
    
# The yield keyword is used to return a list of values from a function.

# Unlike the return keyword which stops further execution of the function, the yield keyword continues to the end of the function.