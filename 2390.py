#2390. Removing Stars From a String - obata1
class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        list_s = []
        for char in s:
            if char != '*':
                list_s.append(char)
            elif list_s:
                list_s.pop()
        return ''.join(list_s)
