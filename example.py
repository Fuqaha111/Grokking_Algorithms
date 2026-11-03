def find_smallest(numbers):
    smallest = numbers[0]
    smallest_index = 0

    for i, n in enumerate(numbers[1:], start=1):
        if smallest > n:
            smallest = n
            smallest_index = i

    return smallest_index

def selection_sort(numbers):
    sorted_list = []
    for i in range(len(numbers)):
        smallest = find_smallest(numbers)
        sorted_list.append(numbers.pop(smallest))
    return sorted_list



print(selection_sort([1, 5, 21, 2, 5, 8, 0]))