# 1512. Number of Good Pairs
class Solution(object):
    def numIdenticalPairs(self, nums):
        k=0
        for a in nums:
            for b in nums[1:]:
                if a == b:
                    k=k+1
            nums=nums[1:]
        return k
