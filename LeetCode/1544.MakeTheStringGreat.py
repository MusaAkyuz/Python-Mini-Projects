class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """

        """
        Mission
        Given a string s of lower and upper case English letters.

        A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where:

        0 <= i <= s.length - 2
        s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa.
        To make the string good, you can choose two adjacent characters that make the string bad and remove them. 
        You can keep doing this until the string becomes good.

        Return the string after making it good. The answer is guaranteed to be unique under the given constraints.

        Notice that an empty string is also good.
        """

        # if s has less than 2 characters, we just return itself.
        while len(s) > 1:
            # 'find' records if we find any pair to remove.
            find = False
            
            # Check every two adjacent characters, curr_char and next_char.
            for i in range(len(s) - 1):
                curr_char, next_char = s[i], s[i + 1]
                
                # If they make a pair, remove them from 's' and let 'find = True'.
                if abs(ord(curr_char) - ord(next_char)) == 32:
                    s = s[:i] + s[i + 2:]
                    find = True
                    break
            
            # If we cannot find any pair to remove, break the loop. 
            if not find:
                break
        return s