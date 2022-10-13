class Solution(object):
    
    
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """

        # keeping starting point color
        # it is filling color
        startColor = image[sr][sc]
        
        # helper function
        def fill(r, c, image, startColor):
            # when every helper function called
            # changing color with color value
            image[r][c] = color
            # four directional scanning with recursive
            for [row, col] in [[r-1, c], [r+1, c], [r, c-1], [r, c+1]]:
                if 0 <= row < len(image) and 0 <= col < len(image[0]) and image[row][col] == startColor:
                    fill(row, col, image, startColor)
        
            # same code with for
            # ------------------
            '''
            if no problem
                fill(row - 1, col, image, startColor)
            if no problem
                fill(row + 1, col, image, startColor)
            if no problem
                fill(row, col - 1, image, startColor)
            if no problem
                fill(row, col + 1, image, startColor)
            '''
        # chech the color is same or not
        if startColor == color:
            return image
        # start with starting point
        fill(sr, sc, image, startColor)
        # when all recursions is done
        return image
