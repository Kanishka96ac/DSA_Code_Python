'''
3. Reverse the Order of Items in an Array

Write a Python program to reverse the order of the items in the array.

Sample Output
Original array: array('i', [1, 3, 5, 3, 7, 1, 9, 3])
Reverse the order of the items:
array('i', [3, 9, 1, 7, 3, 5, 3, 1])
'''

from array import *

arr = array('i', [1, 3, 5, 3, 7, 1, 9, 3])

print(arr[: : -1])