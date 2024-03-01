# 1828. Queries on Number of Points Inside a Circle
class Solution(object):
    def countPoints(self, points, queries):
        """
        :type points: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        answer = []
        for j in queries:
            count=0
            for i in points:
                if (i[0]-j[0])**2+(i[1]-j[1])**2 <= j[2]**2:
                    count+=1
            answer.append(count)
        return answer
