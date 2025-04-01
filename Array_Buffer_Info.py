'''
Write a Python program to get the current memory address and the length in elements of the buffer used to hold an array's contents. Also, find the size of the memory buffer in bytes.

Sample Output:
Original array: array('i', [1, 3, 5, 7, 9])
Current memory address and the length in elements of the buffer: (139741883429512, 5)
The size of the memory buffer in bytes: 20
'''

from array import *

numArr = array('i', [1, 3, 5, 7, 9])

#Using 'buffer_info()' and 'itemsize'
print(f'Current memory address and the length in elements of the buffer: {numArr.buffer_info()}')
print(f'The size of the memory buffer in bytes: {numArr.buffer_info()[1] * numArr.itemsize}')