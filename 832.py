# 832. Flipping an Image
class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(image) %2 ==0 :
            r = len(image)/2
        else:
            r = (len(image)-1)/2
        for i in range(len(image)):
            for j in range(len(image)):
                if image[i][j]:
                    image[i][j] = 0
                else:
                    image[i][j] = 1
        for i in range(len(image)):
            for j in range(r):
                if image[i][j]:
                    if image[i][-1-j]:
                        image[i][j] = 1
                    else:
                        image[i][j] = 0
                    image[i][-1-j]=1
                else:
                    if image[i][-1-j]:
                        image[i][j] = 1
                    else:
                        image[i][j] = 0
                    image[i][-1-j]=0
        return image
