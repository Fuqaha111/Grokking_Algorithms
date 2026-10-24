"""
- This function loops through an array
- Every time it passes a number it adds it to the value total
- After the array finishes it return total
"""


def array_sum(arr):
    total = 0
    for number in arr:
        total += number
    return total

numbers = [2, 4, 6]
print(array_sum(numbers))