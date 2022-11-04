class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        """
        Mission
        Given a string s, find the length of the longest 
        substring
        without repeating characters.
        """
        loopback = []
        res = 0
        i = 0

        while i < len(s):
            j = i
            while j < len(s) and s[j] not in loopback:
                loopback.append(s[j])
                j += 1
            res = max(res, len(loopback))
            loopback = []
            i += 1

        return res