def reccursive_sum(arr):

    if arr == []:
        return 0
    else:
        return arr[0] + reccursive_sum(arr[1:])


numbers = [2, 4, 6]
print(reccursive_sum(numbers))