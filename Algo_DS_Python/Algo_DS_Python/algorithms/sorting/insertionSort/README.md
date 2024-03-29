# Insertion Sort & Binary Insertion Sort
### Insertion Sort: O(n<sup>2</sup>):
#### Insertion sort is a simple sorting algorithm that sorts a list by iterating through each item and swapping that item with previous elements in list until the item is in correct spot.
### Example:
##### Start with 2nd item in list and swap with 1st item if smaller.
###### [5,**6**,2,1,7,3,8] => [5,**6**,2,1,7,3,8]
##### Then compare 3rd item with previous items in list and swap if item is smaller 
###### [5,6,**2**,1,7,3,8] => [5,**2**,6,1,7,3,8] => [**2**,5,6,1,7,3,8]
##### Continue down the rest of list swapping items until no item is smaller then previous items.
###### [2,5,6,**1**,7,3,8] => [2,5,**1**,6,7,3,8] => [2,**1**,5,6,7,3,8] => [**1**,2,5,6,7,3,8]
###### [1,2,5,6,**7**,3,8]
###### [1,2,5,6,7,**3**,8] => [1,2,5,6,**3**,7,8] => [1,2,5,**3**,6,7,8] => [1,2,**3**,5,6,7,8]
###### [1,2,3,5,6,7,**8**]