# 13. Roman to Integer - obata1
class Solution(object):
    def romanToInt(self, s):
        hashmap = {}
        hashmap["I"] = 1
        hashmap["V"] = 5
        hashmap["X"] = 10
        hashmap["L"] = 50
        hashmap["C"] = 100
        hashmap["D"] = 500
        hashmap["M"] = 1000
        ans=0
        l = [char for char in s]
        while l:
            pop = l.pop()
            ans += hashmap[pop]
            if l:
                if pop in 'VX':
                    pop = l.pop()
                    if pop == 'I':
                        ans-=1
                    else:
                        l.append(pop)
                elif pop in "LC":
                    pop = l.pop()
                    if pop == 'X':
                        ans-=10
                    else:
                        l.append(pop)
                elif pop in "DM":
                    pop = l.pop()
                    if pop == 'C':
                        ans-=100
                    else:
                        l.append(pop)
        return ans
