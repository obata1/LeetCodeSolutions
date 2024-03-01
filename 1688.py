# 1688. Count of Matches in Tournament
class Solution(object):
    def numberOfMatches(self, n):
        count=0
        while(n>1):
            if(n % 2 ==0):
                n/=2
                count+=n
                
            else:
                count+=(n-1)/2
                n=(n+1)/2
        return count
