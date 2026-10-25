"""
why it works:
1- in case the list the first if satetment returns 0
2- if the list has only one element it will return arr[0] + 0 (the element + 0) which equals to the first element
"""

def reccursive_sum(arr):
    if arr == []:
        return 0
    else:
        return arr[0] + reccursive_sum(arr[1:])

numbers = [2]
print(reccursive_sum(numbers))

