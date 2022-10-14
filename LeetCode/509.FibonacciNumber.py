class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """

        '''
        Mission
        The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that 
        each number is the sum of the two preceding ones, starting from 0 and 1. That is,

        F(0) = 0, F(1) = 1
        F(n) = F(n - 1) + F(n - 2), for n > 1.
        Given n, calculate F(n).
        '''

        def helper(num):
            if num == 0:
                return 0
            elif num == 1:
                return 1
            else:
                return helper(num-1) + helper(num-2)
        
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return helper(n-1) + helper(n-2)
        