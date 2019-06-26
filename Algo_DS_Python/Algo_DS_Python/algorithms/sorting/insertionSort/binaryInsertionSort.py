import math

def binarySearch(arr, x, l, r):
    if(l==r):
        if(arr[l] > x):
            return l
        else:
            return l+1
    
    if(l > r):
        return l

    mid = int( math.ceil((l+r)/2))

    if(arr[mid] == x):
        return mid
    elif(arr[mid] > x):
        return binarySearch(arr, x, l, mid-1)
    else:
        return binarySearch(arr, x, l+1, r)

def binaryInsertionSort(arr):
    for i in range(len(arr)):
        val = arr[i]
        j = binarySearch(arr, val, 0, i-1)
        arr = arr[:j] + [val] + arr[j:i] + arr[i+1:]
    return arr
