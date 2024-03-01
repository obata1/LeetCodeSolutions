# 1021. Remove Outermost Parentheses
class Solution(object):
    def removeOuterParentheses(self, s):
        ans = ""
        par_open, par_close = 0,0
        for i,a in enumerate(s):
            if a == "(":
                par_open+=1
            else:
                par_close+=1
            if par_open == par_close:
                k=par_open+par_close
                ans+=s[1:k-1]
                s = s[k:]
                par_open, par_close= 0,0
        return ans
