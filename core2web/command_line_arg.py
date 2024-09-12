# #command line arguments

# x,y,z=[int(data) for data in input("Enter value: ").split(" ")]
# a=input("Enter values: ").split(" ")  # split return list

# print(type(a))
# print(a)
# print(type(x))
# print(x)
# print(y)
# print(z)

import sys

# print(sys.argv[0])
# print(sys.argv[1])
# print(sys.argv[2])

add=0
size=len(sys.argv)
for i in range(1,size):
    add=add+int(sys.argv[i]) # is add not declare then is show error add not define bacause add scope on for loop only
    
print(add)



