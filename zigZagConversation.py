####
#
# convert string in zigzag order to row by row.
#
# leetcode 6
#
####

def convert(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    if numRows == 1 or numRows>=len(s): return s
    re = ""
    x = math.ceil(len(s) / 2*(numRows-1))
    for h in range(numRows):
        # for i in range(x):
        #     index = i * (2*numRows-2) + h
        for index in range(h, len(s), 2*numRows-2):
            # if index < len(s): re += s[index]
            re += s[index]
            
            if h != 0 and h != numRows-1:
                index2 = index + 2*(numRows-1-h)
                if index2 < len(s): re += s[index2]
    return re