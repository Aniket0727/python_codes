def find_number_of_steps(X, Y):
    current_number = X
    steps = 0
    
    while current_number < Y:
        #steps += 1
        current_number = current_number * 10 + X
    if current_number==X:
        steps=1
    else:
        steps=2
    
    return steps

# Reading input
X = int(input().strip())
Y = int(input().strip())

# Finding number of steps
result = find_number_of_steps(X, Y)

# Outputting the result
print(result)