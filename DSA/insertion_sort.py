
def insertion_sort(a):
    n=len(a)
    for i in range(1, n):
        temp = a[i]
        j = i - 1
        # Move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position
        while j >= 0 and  a[j] > temp:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = temp

# Example usage:
a = [5, 4, 10, 1, 6, 2]
insertion_sort(a)
print("Sorted array is:", a) 