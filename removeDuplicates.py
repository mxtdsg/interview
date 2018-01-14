####
#
# remove duplicates from sorted list. In-place, return length of new list
#
# leetcode 26
#
####

def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 0: return 0
    newi = 0
    for i in range(len(nums)-1):
        if nums[i] != nums[i+1]:
            newi += 1
        nums[newi] = nums[i+1]
    return newi+1