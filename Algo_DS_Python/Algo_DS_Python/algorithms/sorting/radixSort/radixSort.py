def countingRadixSort(arr, r):
    count = [0 for i in range(r)]
    sortedArr = [0 for i in range(len(arr))]
    temp = 0

    for i in arr:
        count[i] += 1

    for i in range(1, len(count)):
        count[i] = count[i] + count[i-1]

    for j in range(len(arr) - 1, -1, -1):
        sortedArr[count[arr[j]] - 1] = arr[j]
        count[arr[j]] -= 1
    return sortedArr

def radixSort(arr):
    max1 = max(arr)
    exp = 1
    while max1/exp > 0:
        countingRadixSort(arr,exp)
        exp *= 10
    return arr

print([5,7,3,45,2,23,56,890,123,45,76,86,12,3,4,5,64,6,14,45,36,337])
print(radixSort([5,7,3,45,2,23,56,890,123,45,76,86,12,3,4,5,64,6,14,45,36,337]))
