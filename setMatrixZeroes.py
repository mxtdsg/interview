####
#
# set the whole row and col 0 when encounter a 0
#
# leetcode 73.
#
# Improv: Use 1st row and col as marker, and 2 bools: O(1) space
#
####

def setZeroes(matrix):
    rows = set()
    cols = set()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                rows.add(j)
                cols.add(i)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if j in rows:
                matrix[i][j] = 0
            if i in cols:
                matrix[i][j] = 0