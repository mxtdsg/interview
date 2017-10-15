###
# DP exsercise 1: 
#   short description: find the min number of coins (given coins in V (a list))
#                     needed to make up a amount S.
#   original source: https://www.topcoder.com/community/data-science/data-science-tutorials/dynamic-programming-from-novice-to-advanced/
#   
#   BUGS encountered: 1.inf 2.unittest assertEqual 
#                     3.index problem (
# 					    a.init need to append can't use index. b.forgot line 21, j needs to be cmaller coins)
#
#   Oct 13 Fri
###



import unittest

def min_coins(V, S):
	N = []
	for n in range(S+1):
		N.append(float('inf'))
	N[0] = 0
	for i in range(S+1):
		for j in V:
			if j<=i:
				if N[i] > N[i-j] + 1:
					N[i] = N[i-j] + 1
	if N[S] != float('inf'):
		return N[S]
	else:
		return -1


class TestMinCoins(unittest.TestCase):
	def test(self):
		self.assertEqual(min_coins([1,3,5], 1), 1)
		self.assertEqual(min_coins([1,3,5], 2), 2)
		self.assertEqual(min_coins([1,3,5], 3), 1)
		self.assertEqual(min_coins([1,3,5], 4), 2)
		self.assertEqual(min_coins([1,3,5], 5), 1)
		self.assertEqual(min_coins([1,3,5], 6), 2)
		self.assertEqual(min_coins([1,3,5], 7), 3)
		self.assertEqual(min_coins([1,3,5], 8), 2)
		self.assertEqual(min_coins([1,3,5], 9), 3)
		self.assertEqual(min_coins([1,3,5], 10), 2)
		self.assertEqual(min_coins([1,3,5], 11), 3)
if __name__ == '__main__':
	unittest.main()

