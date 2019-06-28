def countingSort(arr, r):
    # Creating empty count list of possible values with default value of zero
    count = [0 for i in range(r)]

    sortedArr = [0 for i in range(len(arr))]
    temp = 0
    
    # Counting all values in arr and storing count in count array
    for i in arr:
        count[i] += 1

    # Adding all count values to previous counts
    for i in range(1, len(count)):
        count[i] = count[i] + count[i-1]

    # Looking at arr and sorting values into new array based on in count array
    for j in range(len(arr) - 1, -1, -1):
        sortedArr[count[arr[j]] - 1] = arr[j]
        count[arr[j]] -= 1
        
    return sortedArr




def shiftedCountingSort(arr, r):
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

