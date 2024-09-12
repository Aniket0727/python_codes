# Method Overloading:
# Method overloading refers to defining multiple methods with the 
# same name but different parameters in a class. Python does not support 
# method overloading directly like some other languages (e.g., Java or C++), 
# but you can achieve a similar effect using default parameter values or variable-length argument lists.


class Calculator:
    def add(self, a, b=0):
        return a + b

# Creating an instance of the Calculator class
calc = Calculator()

# Calling the add method with different arguments
print(calc.add(2, 3))  # Output: 5
print(calc.add(2))     # Output: 2 (default value of b is used)
