####
#
# max subarray
#
# leetcode 53.
#
####
def maxSubArray(nums):

    curSum = maxSum = nums[0]
    for num in nums[1:]:
        curSum = max(num, curSum + num)
        maxSum = max(maxSum, curSum)

    return maxSum