import copy

class Solution(object):
    
    """
    Mission
    You are given two images, img1 and img2, represented as binary, square matrices of size n x n. 
    A binary matrix has only 0s and 1s as values.

    We translate one image however we choose by sliding all the 1 bits left, right, up, and/or down 
    any number of units. We then place it on top of the other image. We can then calculate the overlap 
    by counting the number of positions that have a 1 in both images.

    Note also that a translation does not include any kind of rotation. Any 1 bits that are translated 
    outside of the matrix borders are erased.

    Return the largest possible overlap.
    """

    def largestOverlap(self, img1, img2):
        """
        :type img1: List[List[int]]
        :type img2: List[List[int]]
        :rtype: int
        """

        def matchNumFunc(img1, img2):
            matchNum = 0
            for indexp, pos in enumerate(img1):
                for indexi, item in enumerate(pos):
                    if item == 1 and item == img2[indexp][indexi]:
                        matchNum += 1
            return matchNum

        def right(img):
            temp = copy.deepcopy(img)
            for indexp, pos in enumerate(temp):
                i = len(pos) - 1
                while i>= 0:
                    if i == 0:
                        temp[indexp][i] = 0
                    else:
                        temp[indexp][i] = pos[i - 1]
                    i -= 1
            return temp
                    
        def down(img):
            temp = copy.deepcopy(img)
            indexp = 0
            while indexp < len(temp):
                indexi = len(temp) - 1
                while indexi >= 0:
                    if indexi == 0:
                        temp[indexi][indexp] = 0
                    else:
                        temp[indexi][indexp] = temp[indexi - 1][indexp]
                    indexi -= 1
                indexp += 1
            return temp

        def left(img):
            temp = copy.deepcopy(img)
            for indexp, pos in enumerate(img):
                i = len(pos) - 1
                while i >= 0:
                    if i == len(img) - 1:
                        temp[indexp][i] = 0
                    else:
                        temp[indexp][i] = pos[i + 1]
                    i -= 1
            return temp

        IMG1 = copy.deepcopy(img1)
        IMG2 = copy.deepcopy(img2)
        maxNum = 0
    
        n1 = len(img1)
        while n1 >= 0:
            tempImg = copy.deepcopy(img1)
            tempImg2 = copy.deepcopy(img2)

            n2 = len(img1[0])
            while n2 >= 0:
                maxNum = max(maxNum, matchNumFunc(tempImg, IMG2))
                tempImg = right(tempImg)
                maxNum = max(maxNum, matchNumFunc(IMG1, tempImg2))
                tempImg2 = right(tempImg2)
                n2 -= 1
            
            tempImg = copy.deepcopy(img1)
            tempImg2 = copy.deepcopy(img2)
            n2 = len(img1[0])
            while n2 >= 0:
                maxNum = max(maxNum, matchNumFunc(tempImg, IMG2))
                tempImg = left(tempImg)
                maxNum = max(maxNum, matchNumFunc(IMG1, tempImg2))
                tempImg2 = left(tempImg2)
                n2 -= 1

            img1 = down(img1)
            img2 = down(img2)
            n1 -= 1

        return maxNum

