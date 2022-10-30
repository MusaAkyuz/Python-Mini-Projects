class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        
        """
        Mission
        Given the array nums consisting of 2n elements in the form 
        [x1,x2,...,xn,y1,y2,...,yn].

        Return the array in the form [x1,y1,x2,y2,...,xn,yn].
        """

        i = 0
        x = 0
        res = []

        while x < len(nums):
            if i > len(nums) - 1:
                i = i - len(nums) + 1
            res.append(nums[i])
            i += n
            x += 1

        return res