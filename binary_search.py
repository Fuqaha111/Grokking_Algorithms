'''
What the code does:
1- The algorithm has to values L and R initialized as the first and last element in the list
2- the algorithm will use these two values to guess the middle value of the list
3- it will then compare it with the target value 
4- if its less than targeted value that means the the target value is on its right side so L becomes mid + 1
5- if its more than targeted value that means the number is on the left side so R becomes mid - 1
6- steps 2-5 are repeated until the middle value = target value (if only one number remain L = R so the L + R / 2 is the middle value which is the same as L or R)
'''

def binary_search(n, target):
    l = 0
    r = len(n) - 1 

    while l <= r:
        mid = (l+r) // 2 # //2 instead of just /2 because the value must be integer (rounded)

        if n[mid] == target:
            return mid
        
        elif n[mid] > target:
            r = mid - 1
        
        else: 
            l = mid + 1

numbers = [3, 5, 6, 8, 9, 20, 22, 27]

print (binary_search(numbers, 20))