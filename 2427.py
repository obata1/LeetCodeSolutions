# 2427. Number of Common Factors
class Solution(object):
    def commonFactors(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        count = 0
        for i in range(1,min([a,b])+1):
            if not a % i and not b % i :
                count+=1
        return count
