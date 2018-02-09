####
#
# longest substring without repetition
#
# leetcode 3.
#
####

def lengthOfLongestSubstring(self, s):
    lastlocation = {}
    rep = set()
    count = 0
    temp = ""
    
    maxsofar = 0
    resofar = ""
    i = 0
    while i < len(s):
        char = s[i]
        if char not in rep:
            rep.add(char)
            temp += char
            count += 1
            if count > maxsofar:
                maxsofar = count
                resofar = temp
        else:
            lastindex = lastlocation[char]
            rep = set()
            count = 0
            temp = ""
            i = lastindex

        if char not in lastlocation:
            lastlocation[char] = i
        else:
            lastlocation[char] = i
        i+=1
    return maxsofar