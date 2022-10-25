class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """


        """
        Mission
        Given two string arrays word1 and word2, return true if the two arrays represent the same string, 
        and false otherwise.

        A string is represented by an array if the array elements concatenated in order forms the string.
        """

        string1 = ""
        string2 = ""

        for _ in word1:
            string1 += _
        for _ in word2:
            string2 += _
        
        return string1 == string2