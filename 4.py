# 4. Median of Two Sorted Arrays
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merge = nums1 + nums2
        merge.sort()
        m = len(merge)
        if m % 2:
            return merge[m//2]
        else:
            return float(merge[m/2-1]+merge[m/2])/2
