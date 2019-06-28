def countingSort(arr, r):
    count = [0 for i in range(r)]
    result = [0 for i in range(r)]
    temp = 0

    for i in arr:
        count[i] += 1
        print(count)
    print()

    for i in range(len(count) - 1):
        count[i+1] = count[i] + count[i+1]
        print(count)
    print(count)
    print()

    for i in range(len(count)):
        count[i], temp = temp, count[i]
        print(count)
    print()

    sortedArr = arr

    for i in arr:
        sortedArr[count[i]-1] = i
        count[i] -= 1
        print(count)
    print()
    return sortedArr


print(countingSort([5,4,2,6,6,7,3,9,2,8,1,3],10))
