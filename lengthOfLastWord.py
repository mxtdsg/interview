####
#
# length of last word
#
# leetcode 58.
#
# eg. "a "
#
####

def lengthOfLastWord(s):
    s = s.lstrip(' ').rstrip(' ')
    lw = s.split(' ')[-1]
    lw = lw.strip(' ')
    return len(lw)