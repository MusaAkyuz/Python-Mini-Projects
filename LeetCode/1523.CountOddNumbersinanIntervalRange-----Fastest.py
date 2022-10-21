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

        numbersCount = high - low + 1

        # there are 4 situation
        # first num even --- last num odd then result = numbersCount // 2
        # first num even --- last num even then result = numbersCount // 2
        # first num odd --- last num even then result = numbersCount // 2
        # first num odd --- last num odd then result = (numbersCount // 2) + 1

        if low % 2 == 1 and high % 2 == 1:
            return (numbersCount // 2) + 1
        return numbersCount // 2