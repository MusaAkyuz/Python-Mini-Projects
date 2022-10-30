class Solution(object):
    def shortestPath(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """

        """
        You are given an m x n integer matrix grid where each cell is either 0 (empty) 
        or 1 (obstacle). You can move up, down, left, or right from and to an empty cell 
        in one step.

        Return the minimum number of steps to walk from the upper left corner (0, 0) 
        to the lower right corner (m - 1, n - 1) given that you can eliminate at most 
        k obstacles. If it is not possible to find such walk return -1.
        """

        # matrix lengths
        m = len(grid) - 1
        n = len(grid[0]) - 1

        # if k equals to maximum size 
        # return k is minimum longs
        if k >= m + n:
            return m + n

        # initialize
        """
        x position
        y position
        Number of we can destroy 
        step number
        """
        tryWay = [0, 0, k, 0]

        # we have to keep past value of road
        seenWay = set()

        while tryWay:
            i = tryWay.pop(0)
            j = tryWay.pop(0)
            k = tryWay.pop(0)
            s = tryWay.pop(0)

            # check for reach
            if (i, j) == (m, n):
                return s

            # all possible direction scan if not in seen
            for xPos, yPos in [(i, j+1), (i+1, j), (i, j-1), (i-1, j)]:

                # check for border for matrix
                # it can not be under 0 or bigger n or m
                if 0 <= xPos < m+1 and 0 <= yPos < n+1:
                    # check for bricks
                    if k >= grid[xPos][yPos]:
                        # create last pos to check
                        tempStatus = (xPos, yPos, k-grid[xPos][yPos], s+1)
                        if tempStatus[0:3] not in seenWay:
                            seenWay.add(tempStatus[0:3])
                            tryWay.append(tempStatus[0])
                            tryWay.append(tempStatus[1])
                            tryWay.append(tempStatus[2])
                            tryWay.append(tempStatus[3])
        return -1
                             
        