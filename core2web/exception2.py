print("Start code")

try:
    num1=int(input("Enter valur num1: "))
    num2=int(input("Enter valur num2: "))

except ValueError as a:  #for num1
    print("Except 1")
    
try:
    print(num1+num2)
except NameError:       #for num2
    print('Except 2')
    
print("End code")