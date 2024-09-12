import copy

print("Shallow Copy ")
# Original list containing nested lists
original_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Shallow copy
shallow_copied_list = copy.copy(original_list)

# Modify the first sublist in the original list
original_list[0][0] = 100

# Print both lists
print("Original list:", original_list)
print("Shallow copied list:", shallow_copied_list)

print()
print("Deep Copy ")

# Original list containing nested lists
original_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Deep copy
deep_copied_list = copy.deepcopy(original_list)

# Modify the first sublist in the original list
original_list[0][0] = 100

# Print both lists
print("Original list:", original_list)
print("Deep copied list:", deep_copied_list)
