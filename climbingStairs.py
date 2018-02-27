####
#
# number of ways to climb n stairs: you can climb 1 or 2 stairs a time
#
# leetcode 70.
#
####

def climbStairs(n):
    re = []
    re.append(1)
    re.append(2)
    for i in range(2, n):
        re.append(re[i-1] + re[i-2])
    return re[n-1]