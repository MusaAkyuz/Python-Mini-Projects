class Solution(object):
    def longestPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        
        """
        Mission
        You are given an array of strings words. Each element of words consists of two 
        lowercase English letters.

        Create the longest possible palindrome by selecting some elements from words and 
        concatenating them in any order. Each element can be selected at most once.

        Return the length of the longest palindrome that you can create. If it is impossible to 
        create any palindrome, return 0.

        A palindrome is a string that reads the same forward and backward.
        """
        
        reversers = []
        mirrors = []

        while words:
            # delete first element from list and assign to element but reverse 
            element = words.pop(0)[::-1]
            # check the list again is anybosy same with element
            # if str is "aa" and if there is other "aa" in list
            # add reversers list to count two times
            # else just add mirrors list  
            if element in words:
                # append to result list to count polindrome length
                reversers.append(element)
                # find the index of the mirror element
                mirrorIndex = words.index(element)
                # delete this item to from words and append to result list
                # so we can write of any mirror element in polindrome
                # we have to delete from words list to dont want to double check same element
                reversers.append(words.pop(mirrorIndex))
            elif element == element[::-1]:
                mirrors.append(element)
        
        # mirrors list contain only single symetric strings
        # for example ["aa", "bb", "cc"] and we only use one of them in the middle of the polindrome
        # so we are adding +2
        if mirrors:
            return len(reversers) * 2 + 2
        else:
            return len(reversers) * 2
        

            
        
