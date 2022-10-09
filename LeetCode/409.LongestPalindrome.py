class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """

        '''
        Mission
        Given a string s which consists of lowercase or uppercase letters, return the length of the longest 
        palindrome that can be built with those letters.
        Letters are case sensitive, for example, "Aa" is not considered a palindrome here.
        '''

        even = 0 # even letters, we can add every polindromes if we have any odd number
        oddList = [] # bigger than 1 odd numbers, we can add every polindrome
        odd1 = 0 # 1 letters count

        # first creating list which store unique letters in s
        # second creating loop to find each counts them in s
        everyDiffLetters = set(s)
        for item in everyDiffLetters:
            if s.count(item) % 2 == 0:
                even += s.count(item)
            elif s.count(item) % 2 != 0 and s.count(item) > 1:
                oddList.append(s.count(item))
            else:
                odd1 += s.count(item)

        # let think here
        # we can create polindrome with one (big odd number) plus every (odd numbers - 1) 
        # so keep the value of extra even numbers which generated from odd numbers
        # later situation, just adds + 1 to find maximum
        oddBig = sum(oddList) - len(oddList)

        
        # check is it empty oddList
        # if empty we will look for odd1 to complete symetry
        if oddList:
            return oddBig + even + 1
        elif odd1 > 0:
            return even + 1
        else:
            return even



