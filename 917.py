# 917. Reverse Only Letters - obata1
class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        boi = list(s)
        reverse = []
        while boi:
            if boi[0] in alphabet:
                reverse.append(boi[0])
            boi.pop(0)
        ans = list(s)
        for i in range(len(ans)):
            if ans[i] in alphabet:
                temp = reverse.pop()
                ans[i] = temp
        return ''.join(ans)
