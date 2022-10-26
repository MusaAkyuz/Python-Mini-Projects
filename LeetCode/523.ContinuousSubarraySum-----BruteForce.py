class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
 
        """
        Mission
        Given an integer array nums and an integer k, return true if nums has a continuous subarray of size 
        at least two whose elements sum up to a multiple of k, or false otherwise.

        An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.
        """

        for indexi, itemi in enumerate(nums):
            if indexi < len(nums) - 1:
                sum = nums[indexi] + nums[indexi + 1]

                if sum % k == 0:
                    return True
                for _ in nums[indexi + 2:]:
                    sum += _
                    if sum % k == 0:
                        return True
        return False
                
         