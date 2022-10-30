class Solution(object):
    def averageValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        """
        Mission
        Given an integer array nums of positive integers, return the average value of all 
        even integers that are divisible by 3.

        Note that the average of n elements is the sum of the n elements divided by n and rounded 
        down to the nearest integer.
        """
        
        sum = 0
        count = 0
        for item in nums:
            if item % 6 == 0:
                sum += item
                count += 1
                
        if sum == 0:
            return 0
        else:
            return sum // count