# Quicksort
> WorstCase Runtime O(n<sup>2</sup>)
> AverageCase Runtime O(nlog(n))
### The way quickSort works is by using the divide and conquor paradigm to sort an array inplace. It does this by partitioning the array `A[p ,, r]` into two subarrays `A[p..q-1]` and `A[q+1...r]` such that every element of `a[p..q-1]` is less than or equal to `a[q]` and `A[q+1..r]`.
### After partitioning you sort the two subarrays by recursive calls to quicksort.
![](QuickSort.png)
