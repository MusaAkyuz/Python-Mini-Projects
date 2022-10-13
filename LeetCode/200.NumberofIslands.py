class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        '''
        Mission
        Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the 
        number of islands.

        An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
        You may assume all four edges of the grid are all surrounded by water.
        '''

        rowCount = len(grid)
        colCount = len(grid[0])

        # if we found island with 4-directional
        # convert this zero to be sea not an island and increase the island number
        # r and c is a starting point
        def convertZero(r, c):
            grid[r][c] = "0"
            for [x, y] in [[r-1, c], [r+1, c], [r, c-1], [r, c+1]]:
                if 0 <= x < rowCount and 0 <= y < colCount and grid[x][y] == "1":
                    convertZero(x, y)


        numOfIsland = 0

        # in first example this is = 4
        for i in range(rowCount):
            # in first example this is = 5 for every row
            for j in range(colCount):
                # if any find island
                if grid[i][j] == "1":
                    numOfIsland += 1
                    convertZero(i, j)
        return numOfIsland
