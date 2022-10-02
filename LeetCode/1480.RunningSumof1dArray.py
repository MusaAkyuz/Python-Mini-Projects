class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        '''
        Mission
        Given an array nums. 
        We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
        Return the running sum of nums.
        '''
        # create zero list
        result = [0]
        
        # append every for iteration
        # add last value and before value on the result list
        for index, item in enumerate(nums):
            result.append(result[index] + item)
            
        # delete first element which "zero"
        result.pop(0)
        return result

