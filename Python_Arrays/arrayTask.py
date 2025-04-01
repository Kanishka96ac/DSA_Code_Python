'''
1. Create an Array and Access Elements

Write a Python program to create an array of 5 integers and display the array items. Access individual elements through indexes.
'''

from array import *

arr = array('i' , [1, 3, 5, 7, 9]) 

print("Access the array")
for i in arr:
    print(i)

print("Access first three items individually")
print(arr[0])
print(arr[1])
print(arr[2])


#Append a New Item to the End of an Array
#Append 11 at the end of the array:
# New array: array('i', [1, 3, 5, 7, 9, 11])

arr.append(11)
print(arr)