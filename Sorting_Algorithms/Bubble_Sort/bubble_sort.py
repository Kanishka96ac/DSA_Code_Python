arr1 = [12,2,6,7,8,8,10,2,9]

def bubbleSort(arr):
    n = len(arr)
    
    for k in range(0, n):
        for i in range (0, n-k-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1] , arr[i]
    
    return arr

print(bubbleSort(arr1))  