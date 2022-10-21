class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """

        """
        Mission
        Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).
        """

        count = 0
        while high >= low:
            if high % 2 == 1:
                count += 1
            high -= 1

        return count