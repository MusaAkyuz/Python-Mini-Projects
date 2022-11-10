class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """

        """
        Mission
        You are given a string s consisting of lowercase English letters. 
        A duplicate removal consists of choosing two adjacent and equal letters 
        and removing them.

        We repeatedly make duplicate removals on s until we no longer can.

        Return the final string after all such duplicate removals have been made. 
        It can be proven that the answer is unique.   
        """
        
        start = 0
        while start <= len(s) - 2:
            if start + 1 < len(s) and s[start] == s[start + 1]:
                s = s[:start] + s[start + 2:]
                start = 0
            else:
                start += 1
        return s