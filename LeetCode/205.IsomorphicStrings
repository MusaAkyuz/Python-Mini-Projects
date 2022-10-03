class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        '''
        Mission
        Given two strings s and t, determine if they are isomorphic.
        Two strings s and t are isomorphic if the characters in s 
        can be replaced to get t.
        All occurrences of a character must be replaced with another 
        character while preserving the order of characters. No two 
        characters may map to the same character, but a character 
        may map to itself.    
        '''

        if len(s) == len(t):
            # starting point
            # key = first char of s
            # value = first char of t
            dictionary = {s[0]: t[0]}

            for index, item in enumerate(list(s)):
                # item -> t[0], t[1], t[2], t[3] ...

                # if item did not find in the dictionary
                # add the item in dictionary with value
                if dictionary.get(item) is None:
                    if t[index] not in dictionary.values():
                        dictionary[item] = t[index]
                    else:
                        return False
                # otherwise
                # check the correctness
                else:
                    if dictionary.get(item) != t[index]:
                        return False
            return True
