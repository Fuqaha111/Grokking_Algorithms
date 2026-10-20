"""
What the code does?
1- find smallest function goes through each element of the array comparing it with tha smallest if its smaller smallest gets assigned a new value
2- def selection sort assigns the index of the smallest value to tha variable 'smallest' using the find_smallest function
3- it appends that value of the index smallest to a new list and removes from the current list
4- it repeats until all values of old list are empty and returns the new list
"""

def find_smallest(n):
    smallest = n[0]
    smallest_index = 0
    for i in range(1, len(n)):
        if smallest > n [i]:
            smallest = n[i]
            smallest_index = i
    return smallest_index
    
    
def selection_sort(n):
    sorted_numbers = []
    for i in range(len(n)):
        smallest = find_smallest(n)
        sorted_numbers.append(n.pop(smallest))
    return sorted_numbers


numbers = [3, 4, 12, 10, 1, 4]
    
print (selection_sort(numbers))