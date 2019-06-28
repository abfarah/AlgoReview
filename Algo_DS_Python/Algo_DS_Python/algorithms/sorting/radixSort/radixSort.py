def countingRadixSort(A, k, d):

    c = [None] * (k)

    for i in range(0, k):
        #print(i)
        c[i] = 0

    for j in range(0, len(A)):
        c[ int( A[j][-d] ) ] = c[int( A[j][-d] )] + 1

    for i in range(1, k):
        c[i] = c[i] + c[i-1]

    B = [None] * (len(A))

    for j in range(len(A) - 1, -1, -1):
        #print(j)
        B[c[int(A[j][-d])] - 1] = A[j]
        c[int( A[j][-d]) ] = c[int( A[j][-d])] - 1

    return B


def radixSort(A, d):

    B = []
    for i in A:
        B.append(str(i).zfill(d))

    # Now sort based on digits
    for i in range(1, d + 1):
        B = countingRadixSort(B, 10, i)

    for i in range(0, len(B)):
        A[i] = int(B[i])
    
    return A

