"""
1- checks if the array is empty if yes it return 0
2- if not it return the first element of the array + the function for the array wothout the first element
3- it repeats until the list is empty and finaly return for the empty list 0
4- it adds all the elements saved in the stack one by one
"""
def reccursive_sum(arr):
    if not arr :
        return 0
    else:
        return arr[0] + reccursive_sum(arr[1:])

numbers = [2, 4, 6]
print(reccursive_sum(numbers))

"""
In action it looks like this
sum (2, 4, 6)       16

2 + sum (4, 6)      2 + 10

4 + sum 6           6 + 4 = 10

6 + sum []          6 + 0 = 6 from here it goes up while the variables are saved in the stack as incomplete functions
"""
