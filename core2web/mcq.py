
print(input())
a=input("Enter data: ")
b=input("Enter second data: ")
print(a+b+input('Enter new data:'))

a,b=int(input('enter first data: ')),int(input('enter second data: '))
print(a)
print(b)


n=int(input('Enter n: '))
i=1
while i!=n+1:
    print(i)
    i+=1 


x=10

def fun():
    x=20
    print(id(x))
fun()
print(id(x))


def concatentate(*args,separator="-"):
    return separator.join(args)

result1=concatentate("a","b","c")
result2=concatentate("x","y","z",separator=":")
print(result1)
print(result2)


def calculate(a,b):
    return a+b,a-b

add_result,sub_result=calculate(8,3)
print("%d,%d(add_result,sub_result)")

import array
# arr=[]
arr=array.array('u',['A','B','C','D','E','F','G','H','I','J'])
print(arr[0:])