def countingSort(arr, r):
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
