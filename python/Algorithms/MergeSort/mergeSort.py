import math
def merge(l, r, arr):
    nl = len(l)
    nr = len(r)
    i = j = k = 0
    while i < nl and j < nr:
        if l[i] <= r[j]:
            arr[k] = l[i]
            i+=1
        else:
            arr[k] = r[j]
            j+=1
        k+=1
    while i<nl:
        arr[k] = l[i]
        i+=1
        k+=1
    while j<nr:
        arr[k] = r[j]
        j+=1
        k+=1

    return arr

def mergeSort(a):
    n = len(a)
    if n < 2:
        return a
    mid = n//2
    leftArr = a[:mid]
    rightArr = a[mid:]
    leftArr = mergeSort(leftArr)
    rightArr = mergeSort(rightArr)
    return merge(leftArr, rightArr, a)



print(mergeSort([5,2,4,6,1,3]))
