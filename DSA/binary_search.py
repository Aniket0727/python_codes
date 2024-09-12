def binary_search(sorted_list, target):
    left, right = 0, len(sorted_list) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if sorted_list[mid] == target:
            return mid  # Target found, return its index
        elif sorted_list[mid] < target:
            left = mid + 1  # Search in the right half
        else:
            right = mid - 1  # Search in the left half
    
    return -1  # Target not found

# Take input list from the user, separated by spaces
user_list = [item.strip() for item in input("Enter values separated by spaces: ").split()]
user_list.sort()  # Sort the list to use binary search

# Take the number to search for from the user
n = input("Enter Num: ")

# Perform binary search
index = binary_search(user_list, n)

if index != -1:
    print("found")
else:
    print("not found")
