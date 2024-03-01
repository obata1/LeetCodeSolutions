# 367. Valid Perfect Square
class Solution(object):
    def isPerfectSquare(self, num):
        a = num**0.5
        return a == int(a)
