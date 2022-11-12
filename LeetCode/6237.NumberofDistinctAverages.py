class Solution(object):
    def distinctAverages(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        """
        Mission
        You are given a 0-indexed integer array nums of even length.

        As long as nums is not empty, you must repetitively:

        Find the minimum number in nums and remove it.
        Find the maximum number in nums and remove it.
        Calculate the average of the two removed numbers.
        The average of two numbers a and b is (a + b) / 2.

        For example, the average of 2 and 3 is (2 + 3) / 2 = 2.5.
        Return the number of distinct averages calculated using the above process.

        Note that when there is a tie for a minimum or maximum number, any can be removed.
        """
        sorting = sorted(nums)
        res = []
        
        while nums:
            min1 = float(nums.pop(nums.index(max(nums))))
            max1 = float(nums.pop(nums.index(min(nums))))
            average = float((min1 + max1) / 2)
            
            if average not in res:
                res.append(average)
                
        return len(res)