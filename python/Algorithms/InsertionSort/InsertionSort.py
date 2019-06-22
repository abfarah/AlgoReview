def insertionSort(arr):
    for j in range(len(arr)):
        temp = arr[j]
        i = j-1
        while(i>=0 and arr[i]>temp):
            arr[i+1] = arr[i]
            i = i-1
        arr[i+1] = temp
    return arr

print(insertionSort([5,2,4,6,1,3]))
