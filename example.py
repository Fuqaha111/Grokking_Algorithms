def binary_search(target, arr):
    l = 0
    r = len(arr)
    

    while l <= r:
        mid = (l + r) //2
        guess = arr[mid]

        if target == guess:
            return mid
        elif target > guess:
            l = mid + 1
        else:
            r = mid - 1

numbers = [0, 1, 3, 6, 9, 100,  102, 1003, 50000]

print(binary_search(50000, numbers))