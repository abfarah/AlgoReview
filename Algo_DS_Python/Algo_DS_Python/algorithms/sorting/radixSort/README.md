# Radix Sort O(d(n+k))
### d = digits, n = input, d = largest amount of digits in one of the numbers
### RadixSort sorts a limited imput by using a stable sub-routine sorting algorithm. 
### It runs through the array d times where d is the largest digit number  `D < {1,10,100,1000,...,}.`
### It then runs through the and sorts based on the last digit to the first digit. 
### for example:
```
[1, 32, 54, 28, 320, 597] --> [320, 1, 32, 54, 597, 28] on the first pass 
[1, 28, 320, 54, 597] --> on the second pass
[1, 28, 54, 320, 597] --> on the last pass.
```
### D in this case is 3 becuase the largest digit place is 100th.
### The time complexity of this sorting algorith is `O(d*(n+b))` where d is the length of the digit place and n is how long it takes because of counting Sort sub routine runs O(n + K) where k is the largest number. k = B is the base number. in this case B would be 10 becuase the numbers are base 10. 
