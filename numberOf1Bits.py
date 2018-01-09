####
#
# input a integer, output the number of 1's in binary rep
#
####


import unittest

def numberOf1Bits(n):
    res = 0
    while n != 0:
        div = n/2
        mod = n%2
        n = div
        if mod != 1:
            continue
        res += 1
    return res

class TestNumberOf1Bits(unittest.TestCase):
    def test(self):
        self.assertEqual(numberOf1Bits(0), 0)
        self.assertEqual(numberOf1Bits(13), 3)
        self.assertEqual(numberOf1Bits(2), 1)
        self.assertEqual(numberOf1Bits(2**9), 1)

if __name__ == '__main__':
    unittest.main()