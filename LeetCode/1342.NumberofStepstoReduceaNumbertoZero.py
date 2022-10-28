class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """

        """
        Mission
        Given an integer num, return the number of steps to reduce it to zero.

        In one step, if the current number is even, you have to divide it by 2, otherwise, you have to 
        subtract 1 from it.
        """

        count = 0
        while num > 0:
            if num%2 == 0:
                num = num/2
                count += 1
            else:
                num = num-1
                count += 1
        return count