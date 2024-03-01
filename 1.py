# 1. Two Sum
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i,a in enumerate(nums):
            for j,b in enumerate(nums):
                if a + b == target and i != j:
                    return [i,j]
