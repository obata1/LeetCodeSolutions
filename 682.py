# 682. Baseball Game
class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        pt = []
        for op in operations:
            if op == '+':
                pt.append(pt[-1]+pt[-2])
            elif op == 'D':
                pt.append(2*pt[-1])
            elif op == 'C':
                pt.pop()
            else:
                pt.append(int(op))
        return sum(pt)
                
