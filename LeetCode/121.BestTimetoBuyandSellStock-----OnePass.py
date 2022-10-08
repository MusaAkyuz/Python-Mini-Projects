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

        maxProfit = 0
        # prices never bigger than this number
        min = 9999999

        for item in prices:
            if item < min:
                # update min
                min = item
            else:
                # calculating profit for every big number item from min
                profit = item - min
                # checking any other profits are big or not
                maxProfit = max(maxProfit, profit)
        return maxProfit