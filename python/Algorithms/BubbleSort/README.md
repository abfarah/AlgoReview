# Bubble Sort O(n<sup>2</sup>)
#### Bubble sort is a very simple sorting algorithm that repeatedly swaps adjacent elements if they are in wrong order.
### Example:
##### First Pass: [**5,6**,2,1,7,3,8] => [5,**6,2**,1,7,3,8] => [5,2,**6,1**,7,3,8] => [5,2,1,**6,7**,3,8] => [5,2,1,6,**7,3**,8] => [5,2,1,6,3,**7,8**] => [5,2,1,6,3,7,8]
##### Second Pass: [**5,2**,1,6,3,7,8] => [2,**5,1**,6,3,7,8] => [2,1,**5,6**,3,7,8] => [2,1,5,**6,3**,7,8] => [2,1,5,3,**6,7**,8] => [2,1,5,3,6,**7,8**] => [2,1,5,3,6,7,8]
##### Third Pass: [**2,1**,5,3,6,7,8] => [1,**2,5**,3,6,7,8] => [1,2,**5,3**,6,7,8] => [1,2,3,**5,6**,7,8] => [1,2,3,5,**6,7**,8] => [1,2,3,5,6,**7,8**] => [1,2,3,5,6,7,8]
##### Final Pass: Finishes when we traverse the whole list without any swaps.
