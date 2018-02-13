####
#
# all permutations of a li
#
# leetcode 46.
#
####

def permute(nums):
    re = [[]]
    for n in nums:
        temp = []
        for el in re:
            for i in xrange(len(el)+1):
                temp.append(el[:i] + [n] + el[i:])
        re = temp
    return re