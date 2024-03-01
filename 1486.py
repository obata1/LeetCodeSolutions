# 1486. XOR Operation in an Array
class Solution(object):
    def xorOperation(self, n, start):
        x=0
        for i in range(n):
            x=x^(start+2*i)
        return x
