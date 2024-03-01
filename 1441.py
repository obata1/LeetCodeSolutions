# 1441. Build an Array With Stack Operations
class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        stack = []
        ops = []
        for i in range(1,n+2):
            if stack == target:
                return ops
            stack.append(i)
            ops.append("Push")
            if i not in target:
                stack.pop()
                ops.append("Pop")
