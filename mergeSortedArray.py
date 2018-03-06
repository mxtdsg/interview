####
#
# merge sorted array m2 to m1 . in-place
#
# leetcode 88.
#
####

def merge(nums1, m, nums2, n):

    i = j = 0
    while i < m or j < n:
        if i > m-1:
            nums1[i:] = nums2[j:]
            break
        if j > n-1:
            break
        if nums1[i] <= nums2[j]:
            i+=1
        else:
            nums1[i+1:i+1+(m-i)] = nums1[i:i+(m-i)]
            nums1[i] = nums2[j]
            i+=1
            m+=1
            j+=1
