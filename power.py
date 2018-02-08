####
#
# computer pow(x, n). log(n) time 
#
# leetcode 50
#
####

def myPow(self, x, n):
    if n == 0:
        return 1
    if n < 0:
        x = 1 / x
        n = -1 * n

    re = 1
    while n > 0:
        if n & 1:
            re *= x
        x *= x
        n >>= 1
    return re