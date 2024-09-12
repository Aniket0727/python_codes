def fun():
    print("start fun")
    yield 10
    yield 20
    yield 30
    print("end fun")
    yield ""
    
    
ret=fun()

print(next(ret))
print(next(ret))
print(next(ret))
print(next(ret))


