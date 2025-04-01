'''
6. Count occurrences of a specified element in an array

Write a Python program to get the number of occurrences of a specified element in an array.

Sample Output:
Original array: array('i', [1, 3, 5, 3, 7, 9, 3])
Number of occurrences of the number 3 in the said array: 3
'''

from array import *

arr = array('i' , [1, 3, 5, 3, 7, 9, 3])

print(f'Original Array: {arr}')

num = 3
tot = 0
for i in arr:
    if i == num:
        tot +=1
print(f'Number of occurrences of the number {num} in the said array: {tot}')

#Or you can directly use 'arr.count(3)'