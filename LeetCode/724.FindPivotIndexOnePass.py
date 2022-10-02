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
        
        # starting ofset is 0(zero)
        # so rightSum = nums[1] + ... + nums[n]
        # leftSum = 0 because there is no element of the left
        rightSum = sum(nums[1:])
        print(rightSum)
        leftSum = 0
        
        # one pass for iteration
        for index, item in enumerate(nums):
            # checking
            if leftSum == rightSum:
                return index
            # every else situation
            # change ofset += 1
            # so adding lelftSum one by one
            # and substruct rightSum one by one until end of index
            leftSum += item
            if index != len(nums) - 1:
                rightSum -= nums[index + 1]
        # if there is no matches retrurn -1
        return -1  







      
            