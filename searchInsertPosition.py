####
#
# search insert position 
#
# leetcode 35
#
####

def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if nums[0] > target: return 0
    if nums[-1] < target: return len(nums)
    for i in range(len(nums)):
        if nums[i] == target:
            return i

        if i < len(nums)-1 and nums[i] < target and nums[i+1] > target:
            return i+1
