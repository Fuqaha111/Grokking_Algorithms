def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        more = [i for i in arr [1:] if i > pivot]

        return quicksort(less) + [pivot] + quicksort(more)
    
numbers = [2, 1, 0, 5, 7, 8, 2]
print (quicksort(numbers))