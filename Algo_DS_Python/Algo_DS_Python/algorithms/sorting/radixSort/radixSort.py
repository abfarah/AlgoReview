def countingSort(arr, r):
    count = [0 for i in range(r+1)]
    result = [ 0 for i in range(len(arr))]

    for i in arr:
        count[i] += 1

    for i in range(1, len(count)):
        count[i] = count[i] + count[i-1]

    # Shifiting all counts to the right in count array
    for i in range(len(count) -1, -1, -1):
        if i <= 0:
            count[i] = 0
        else:
            count[i] = count[i-1]

    for i in arr:
        result[count[i]] = i
        count[i] +=1

    return result

def radixSort(arr):
    max1 = max(arr)
    exp = 1
    while max1/exp > 0:
        countingSort(arr,exp)
        exp *= 10
    return arr

print([5,7,3,45,2,23,56,890,123,45,76,86,12,3,4,5,64,6,14,45,36,337])
print(radixSort([5,7,3,45,2,23,56,890,123,45,76,86,12,3,4,5,64,6,14,45,36,337]))
