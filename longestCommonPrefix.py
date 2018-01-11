####
#
# find the longest common prefix of a list of strs
#
# leetcode 14.
#
####


def longestCommonPrefix(strs):
    if len(strs) == 0: return ""
    minlength = min([len(st) for st in strs])
    re = ""
    for i in range(minlength):
        for st in strs:
            if st[i] != strs[0][i]:
                return re
        re += strs[0][i]
    return re