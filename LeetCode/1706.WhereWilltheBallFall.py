class Solution(object):
    def findBall(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """

        res = []
        n = len(grid[0])
        m = len(grid)
        # row goes [0] to [len(grid) - 1]
        # column goes to [0] to [len(grid[0])]
        row = 0
        column = 0

        for _ in range(n):
            tempRow = row
            tempColumn = column
            for __ in range(m):
                if grid[tempRow][tempColumn] == 1:
                    if 0 <= tempColumn + 1 < len(grid[0]) and grid[tempRow][tempColumn + 1] == 1:
                        tempRow += 1
                        tempColumn += 1
                    else:
                        tempColumn = -1
                        break
                elif grid[tempRow][tempColumn] == -1:
                    if 0 <= tempColumn - 1 < len(grid[0]) and grid[tempRow][tempColumn - 1] == -1:
                        tempRow += 1
                        tempColumn -= 1
                    else:
                        tempColumn = -1
                        break
            res.append(tempColumn)
            column += 1
        return res