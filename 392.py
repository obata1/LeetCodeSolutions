# 392. Is Subsequence
class Solution(object):
    def isSubsequence(self, s, t):
        k=0
        for a in s:
            for i,b in enumerate(t):
                if a == b:
                    k=k+1
                    t=t[i+1:]
                    break
        return k == len(s)
