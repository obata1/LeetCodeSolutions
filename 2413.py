# 2413. Smallest Even Multiple
class Solution(object):
    def smallestEvenMultiple(self, n):
        for i in range(1,2*n+1):
            if i % n == 0 and i % 2 == 0:
                return i
