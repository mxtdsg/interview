####
#
# group anagrams in alpha. order
#
# leetcode 49.
#
####

def groupAnagrams(strs):
    d = {}
    for w in sorted(strs):
        key = tuple(sorted(w))
        d[key] = d.get(key, []) + [w]
    return d.values()