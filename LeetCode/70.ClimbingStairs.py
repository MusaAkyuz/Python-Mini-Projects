class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        '''
        Mission
        You are climbing a staircase. It takes n steps to reach the top.
        Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
        '''
        '''
        n = 1 için unique = 1
        n = 2 için unique = 2
        n = 3 için unique = 3
        n = 4 için unique = 5
        n = 5 için unique = 8
        answer is sum of last two step
        '''

        if n==0: return 0
        if n==1: return 1
        if n==2: return 2
        dp = [0]*(n+1) # considering zero steps we need n+1 places
        dp[1]= 1
        dp[2] = 2
        for i in range(3,n+1):
            dp[i] = dp[i-1] +dp[i-2]
        print(dp)
        return dp[n]