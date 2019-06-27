from bubbleSort import bubbleSort
from insertionSort import insertionSort
from binaryInsertionSort import binaryInsertionSort
from mergeSort import mergeSort
from selectionSort import selectionSort
from quickSort import quickSort
from quickSort.quickSort import randomized_quickSort

import unittest

class test(unittest.TestCase): 
    arr = [5,12,8,18,16,19,6,13,2,10,20,15,7,9,14,3,11,1,17,4]
    sortedArr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    def test_BubbleSort(self):
        self.assertEqual(bubbleSort.bubbleSort(test.arr),test.sortedArr)

    def test_insertionSort(self):
        self.assertEqual(insertionSort.insertionSort(test.arr),test.sortedArr)

    def test_binaryInsertionSort(self):
        self.assertEqual(binaryInsertionSort.binaryInsertionSort(test.arr),test.sortedArr)

    def test_mergeSort(self):
        self.assertEqual(mergeSort.mergeSort(test.arr),test.sortedArr)

    def test_selectionSort(self):
        self.assertEqual(selectionSort.selectionSort(test.arr),test.sortedArr)

    def test_quickSort(self):
        self.assertEqual(quickSort.quickSort(test.arr, 0, len(test.arr) - 1),test.sortedArr)

    def test_randomized_quickSort(self):
        self.assertEqual(quickSort.randomized_quickSort(test.arr, 0, len(test.arr) - 1),test.sortedArr)

if __name__ == '__main__': 
    unittest.main()
