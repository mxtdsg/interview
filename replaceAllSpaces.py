####
#
# leetcode 1.5
#
# Replace all spaces in a string with '%20'
#
####

import unittest

def replaceAllSpaces(string):
    i = 0
    while i < len(string):
        if string[i] != " ":
            i+=1
        else:
            string = string.replace(" ", "%20")
            i+=3
    return string


class TestReplaceAllSpaces(unittest.TestCase):
    def test(self):
        self.assertEqual(replaceAllSpaces("hello world"), "hello%20world")
        self.assertEqual(replaceAllSpaces("helloworld"), "helloworld")
        self.assertEqual(replaceAllSpaces(""), "")
        self.assertEqual(replaceAllSpaces(" "), "%20")
        self.assertEqual(replaceAllSpaces("   "), "%20%20%20")


if __name__ == '__main__':
    unittest.main()