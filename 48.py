# 48. Rotate Image
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(i,len(matrix)):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        for i in range(len(matrix)):
            for j in range(len(matrix)//2):
                temp = matrix[i][j]
                matrix[i][j] = matrix[i][-1-j]
                matrix[i][-1-j] = temp
        return matrix
