from array import *
arr = array('i', [4, 3, 1, 6, 8, 5])

#Add element into the end of the Array
arr.append(12)

#Add element into the given index of the array
arr.insert(2, 99)

#add another array into end of the array
arr.extend([11,22,33,44])

print(arr)


'''
Traversal Operation
'''

for i in arr:
    print(i)
    
    
#Access array elements

print('5th Index is : ',arr[5])


#Delete the last element of the array 
print(arr)
print(f'print pop {arr.pop()}')

#Delete the given value of the array (You should give the value which need to remove not the index)
print(arr)
print(f'print remove {arr.remove(99)}')
print(arr)
