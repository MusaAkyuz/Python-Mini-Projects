class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """ 
        
        '''
        ---One Pass---
        Creating hash map with value and index of all elements in nums
        It helps to only one time pass on index
        we will check the differences to reach the target
        and control the hash map
        '''
        # we will keep index : value
        hashMap = {}
        
        # index showing the index of item in nums list
        # item show the item itself in nums list
        for index, item in enumerate(nums):
            
            # diff that we are looking for it
            # if any in the hash map, we will found
            diff = target - item
            
            # checking hashmap to any matches num
            if diff in hashMap:
                return [hashMap[diff], index]
            
            # if not we are saving to hashmap for after
            hashMap[item] = index
        return 