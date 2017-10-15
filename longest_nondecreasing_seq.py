###
# DP exsercise 2: 
#   short description: Given int list A, find the longest non-decreasing sequence ends at I.
#
#   original source: https://www.topcoder.com/community/data-science/data-science-tutorials/dynamic-programming-from-novice-to-advanced/
#   
#   BUGS encountered: 1.naming can't have '-' 2.handling Last, line 23, 28.
# 
#   Oct 14 Sat
###


import unittest

def longest_nondecreasing_seq(A, I):
	### return tuple for testing: (longest, lastNumberInSeq)
	N = len(A)
	L = []
	Last = []
	for i in range(N):
		L.append(1)
		Last.append(float("inf"))
	Last[0] = A[0]
	for i in range(I):
		for j in range(i):
			if ((L[j]+1 > L[i]) and Last[j] <= A[i]) or (L[i]==0 and A[i]>=A[j]):
				L[i] = L[j] + 1
				Last[i] = A[i]

			else: Last[i] = A[i]

	return (L[I-1], Last[I-1])

class TestLongest(unittest.TestCase):
	def test(self):
		self.assertEqual(longest_nondecreasing_seq((5, 3, 4, 8, 6, 7), 1), (1,5))
		self.assertEqual(longest_nondecreasing_seq((5, 3, 4, 8, 6, 7), 2), (1,3))
		self.assertEqual(longest_nondecreasing_seq((5, 3, 4, 8, 6, 7), 3), (2,4))
		self.assertEqual(longest_nondecreasing_seq((5, 3, 4, 8, 6, 7), 4), (3,8))
		self.assertEqual(longest_nondecreasing_seq((5, 3, 4, 8, 6, 7), 5), (3,6))
		self.assertEqual(longest_nondecreasing_seq((5, 3, 4, 8, 6, 7), 6), (4,7))

		self.assertEqual(longest_nondecreasing_seq((5, 3, 4, 8, 9, 6, 7), 6), (4,9))

if __name__ == '__main__':
	unittest.main()