# Bubble sort algorithm

def bubble_sort(a): 
    n = len(a)
    for i in range(n):
        for j in range(n -1):
            if a[j] > a[j + 1]:
                # Swap elements
                a[j], a[j + 1] = a[j + 1], a[j]


a=[6,4,8,1,2,9,0]
bubble_sort(a)
print("Sorted list:", a)
