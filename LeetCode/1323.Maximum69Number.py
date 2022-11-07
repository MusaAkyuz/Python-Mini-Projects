class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """

        """
        Mission
        You are given a positive integer num consisting only of digits 6 and 9.

        Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6). 
        """
        strn = str(num)
        for i in range(len(strn)):
            if strn[i] == "6":
                return int(strn[:i] + "9" + strn[i + 1:])

        return num
