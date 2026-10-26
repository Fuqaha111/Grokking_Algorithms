"""
what the code does:
- it goes throgh each elemnt of the array and adds it to the total
"""

def array_sum(arr):
    total = 0
    for i in range(len(arr)):
        total += arr[i]
    return total

numbers = [2, 4, 6]
print(array_sum(numbers))