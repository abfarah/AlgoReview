from karpRabin.kr import karpRabin

import unittest

class test(unittest.TestCase):
    s = "test"
    t = "This is a test string. test test test"
    result  = "4 matches found at indexes [[10, 14], [23, 27], [28, 32], [33, 37]]"
    def test_karpRabin(self):
        self.assertEqual(karpRabin(test.s, test.t),test.result)

if __name__ == '__main__': 
    unittest.main()
