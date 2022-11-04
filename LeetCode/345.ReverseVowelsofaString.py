class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        """
        Mission
        Given a string s, reverse only all the vowels in the string and return it.

        The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and 
        upper cases, more than once.
        """

        vowel = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        s = list(str(s))
        print(s)
        left = 0
        right = len(s) - 1
        i = 0

        while left <= right:
            if s[left] in vowel:
                if s[right] in vowel:
                    temp = s[left]
                    s[left] = s[right]
                    s[right] = temp
                    right -= 1
                    left += 1
                else:
                    right -= 1
            else:
                left += 1
            i += 1

        return "".join(s)
