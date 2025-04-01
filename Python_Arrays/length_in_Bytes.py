'''
4. Get the Length in Bytes of One Array Item

Write a Python program to get the length in bytes of one array item in the internal representation.

Sample Output:
Original array: array('i', [1, 3, 5, 7, 9])
Length in bytes of one array item: 4
'''

from array import *

arr = array('i', [1, 3, 5, 7, 9])

print("Original array: "+str(arr))
#Using 'itemsize'
print("Length in bytes of one array item: "+str(arr.itemsize))