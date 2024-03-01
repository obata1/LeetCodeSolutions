# 844. Backspace String Compare - obata1
class Solution(object):
    def backspaceCompare(self, s, t):
        list_s,list_t = [],[]
        for char in s:
            if char != '#':
                list_s.append(char)
            elif list_s:
                list_s.pop()
        for char in t:
            if char != '#':
                list_t.append(char)
            elif list_t:
                    list_t.pop()
        return list_s == list_t
