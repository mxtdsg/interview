### 
#
# First letter appearing twice in a given stirng
#
# Review: 1. Python dictionary: hash mapping / hash table 
#         2. On average, hash table: space O(n), seach/insert/delete O(1)
#
# Source: https://www.youtube.com/watch?v=GJdiM-muYqc&index=10&list=WL
#
###



import unittest

def first_recurring(given_str):
    dic = {}
    for char in given_str:
        if char not in dic:
            dic[char] = 0
        else:
            return char
    return None


class TestFirstRecurring(unittest.TestCase):
    def test_rec(self):
        self.assertEqual(first_recurring("DBCABA"), 'B')
        self.assertEqual(first_recurring("ABCA"), 'A')
        self.assertEqual(first_recurring("BCABA"), 'B')
        self.assertEqual(first_recurring("ABC"), None)

if __name__ == '__main__':
    unittest.main()