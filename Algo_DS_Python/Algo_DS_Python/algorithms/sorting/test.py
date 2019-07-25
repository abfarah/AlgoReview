from bubbleSort.bubbleSort import bubbleSort
from insertionSort.insertionSort import insertionSort
from binaryInsertionSort.binaryInsertionSort import binaryInsertionSort
from mergeSort.mergeSort import mergeSort
from selectionSort.selectionSort import selectionSort
from quickSort.quickSort import quickSort
from quickSort.quickSort import randomized_quickSort
from countingSort.countingSort import countingSort
from countingSort.countingSort import shiftedCountingSort
from radixSort.radixSort import radixSort

import unittest

class test(unittest.TestCase): 
    arr = [5,12,8,18,16,19,6,13,2,10,20,15,7,9,14,3,11,1,17,4]
    sortedArr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    def test_BubbleSort(self):
        self.assertEqual(bubbleSort(test.arr),test.sortedArr)

    def test_insertionSort(self):
        self.assertEqual(insertionSort(test.arr),test.sortedArr)

    def test_binaryInsertionSort(self):
        self.assertEqual(binaryInsertionSort(test.arr),test.sortedArr)

    def test_mergeSort(self):
        self.assertEqual(mergeSort(test.arr),test.sortedArr)

    def test_selectionSort(self):
        self.assertEqual(selectionSort(test.arr),test.sortedArr)

    def test_quickSort(self):
        self.assertEqual(quickSort(test.arr, 0, len(test.arr) - 1),test.sortedArr)

    def test_randomized_quickSort(self):
        self.assertEqual(randomized_quickSort(test.arr, 0, len(test.arr) - 1),test.sortedArr)

    def test_countingSort(self):
        self.assertEqual(countingSort(test.arr, 21),test.sortedArr)

    def test_shiftedCountingSort(self):
        self.assertEqual(shiftedCountingSort(test.arr, 20),test.sortedArr)

    def test_radixSort(self):
        self.assertEqual(radixSort(test.arr, 20),test.sortedArr)

if __name__ == '__main__': 
    unittest.main()
