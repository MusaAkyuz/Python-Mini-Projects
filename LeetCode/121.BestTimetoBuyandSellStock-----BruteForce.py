class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        '''
        Mission
        You are given an array prices where prices[i] is the price of a given 
        stock on the ith day.
        You want to maximize your profit by choosing a single day to buy one stock 
        and choosing a different day in the future to sell that stock.
        Return the maximum profit you can achieve from this transaction. If you 
        cannot achieve any profit, return 0
        '''

        # creating profit dictionary
        profDic = {-1: 0}

        # creating loop to adding in dictionary all profits
        for index, item in enumerate(prices):
            # finding max profits for every index
            maxProfit = max(prices[index:]) - item
            # filtering unnecessary values which negative
            if maxProfit > 0:
                profDic[index] = maxProfit

        return max(profDic.values())