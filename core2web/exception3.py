list1=[10,'annu',20,'aniket']

try:
    index1=int(input("Enter index1: "))
    print(list1[index1])
    
    index2=int(input("Enter index2: "))
    print(list1[index2])
    
    add=list1[index1]+list1[index2]
except ValueError as e:
    print("ValueError error handled")
    print(e)

except IndexError as e:
    print("IndexError error handled")
    print(e)

except TypeError as e:
    print("TypeError error handled")
    print(e)
    
else:      #else block will execute if no exceptions are raised in the try block.
    print(add)
    
print("End Code")