import random

def partition(arr, l, r):
    x = arr[r]
    i = l - 1
    for j in range(l, r):
        if arr[j] <= x:
            i +=1
            arr[j], arr[i] = arr[i], arr[j]
    arr[i+1], arr[r] = arr[r], arr[i+1]
    return i+1

def quickSort(arr, l, r):
    if l < r:
        q = partition(arr,l,r)
        quickSort(arr, l, q-1)
        quickSort(arr, q+1, r)
        return arr

def randomized_partition(arr, l, r):
    i = random.randint(l,r)
    arr[i], arr[r]  = arr[r], arr[i]
    return partition(arr, l, r)

def randomized_quickSort(arr, l, r):
    if l < r:
        q = randomized_partition(arr, l, r)
        randomized_quickSort(arr, l, q-1)
        randomized_quickSort(arr, q+1, r)
        return arr
