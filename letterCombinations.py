####
#
# return all the mapping combinations of the given digits
#
# leetcode 17.
#
####

def letterCombinations(self, digits):
    dic = {"2":"abc", "3": "def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
    re = [""]
    temp = []
    for digit in digits:
        temp = []
        for el in re:
            for char in dic[digit]:
                temp.append(el+char)
        re = temp
    return temp