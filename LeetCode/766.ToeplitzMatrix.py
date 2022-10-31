class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        
        """
        Mission
        Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.

        A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.
        """

        for index, lis in enumerate(matrix):
            if index < len(matrix) - 1:
                if not lis[:len(matrix[0]) - 1] == matrix[index + 1][1:]:
                    return False
        return True

