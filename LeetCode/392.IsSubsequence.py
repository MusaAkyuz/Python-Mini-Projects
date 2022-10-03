class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        '''
        Mission
        Given two strings s and t, return true if s is a subsequence of t, 
        or false otherwise.
        A subsequence of a string is a new string that is formed from the 
        original string by deleting some (can be none) of the characters 
        without disturbing the relative positions of the remaining characters. 
        (i.e., "ace" is a subsequence of "abcde" while "aec" is not). 
        '''
        # convert main string to list
        list_t = list(t)
        list_s = list(s)

        # ofset store data the last index on list_t
        # so we will check after from ofset to mission
        ofset = 0
        for index, item in enumerate(list_s):
            # index -> 0, 1, 2, 3, ...
            # item -> s[0], s[1], ...
            
            # checking after from ofset
            # if nobody matches return false
            # if item matches, jump to another item
            # and change the ofset 
            if item in list_t[ofset:]:
                ofset = list_t.index(item, ofset) + 1
            else:
                return False
        return True