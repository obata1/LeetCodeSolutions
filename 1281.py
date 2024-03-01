# 1281. Subtract the Product and Sum of Digits of an Integer
class Solution(object):
    def subtractProductAndSum(self, n):
        s,p = 0,1
        for i in range(5):
            s+=int(n/10**(4-i))-10*int(n/10**(5-i))
            if n > 10**(4-i):
                p*=int(n/10**(4-i))-10*int(n/10**(5-i))
        return p-s
