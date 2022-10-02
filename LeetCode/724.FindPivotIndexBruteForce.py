class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        '''
        Mission
        Given an array of integers nums, calculate the pivot index of this array.
        The pivot index is the index where the sum of all the numbers strictly to 
        the left of the index is equal to the sum of all the numbers strictly to the 
        index's right.
        If the index is on the left edge of the array, then the left sum is 0 because 
        there are no elements to the left. This also applies to the right edge of 
        the array.
        Return the leftmost pivot index. If no such index exists, return -1.
        '''
        
        # try for every index
        # starting 0 and calculates for every left right
        for index in range(len(nums)):
            leftSum = 0
            rightSum = 0

            # leftSum
            temp = index - 1
            while temp >= 0:
                leftSum += nums[temp]
                temp -= 1

            #rightSum
            temp = index + 1
            while temp <= len(nums) - 1:
                rightSum += nums[temp]
                temp += 1
            
            if leftSum == rightSum:
                return index
        # if did not return for all case 
        return -1
