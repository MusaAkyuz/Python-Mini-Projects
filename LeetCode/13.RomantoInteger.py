class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        """
        Mission
        Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

        Symbol       Value
        I             1
        V             5
        X             10
        L             50
        C             100
        D             500
        M             1000
        For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, 
        which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

        Roman numerals are usually written largest to smallest from left to right. However, the numeral for 
        four is not IIII. Instead, the number four is written as IV. Because the one is before the five we 
        subtract it making four. The same principle applies to the number nine, which is written as IX. There 
        are six instances where subtraction is used:

        I can be placed before V (5) and X (10) to make 4 and 9. 
        X can be placed before L (50) and C (100) to make 40 and 90. 
        C can be placed before D (500) and M (1000) to make 400 and 900.
        Given a roman numeral, convert it to an integer.
        """

        #romans = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        sum = 0
        i = 0
        while i < len(s):
            if s[i] == "M":
                if i > 0 and s[i - 1] == "C":
                    sum -= 200
                sum += 1000
            if s[i] == "D":
                if i > 0 and s[i - 1] == "C":
                    sum -= 200
                sum += 500
            if s[i] == "C":
                if i > 0 and s[i - 1] == "X":
                    sum -= 20
                sum += 100
            if s[i] == "L":
                if i > 0 and s[i - 1] == "X":
                    sum -= 20
                sum += 50
            if s[i] == "X":
                if i > 0 and s[i - 1] == "I":
                    sum -= 2
                sum += 10
            if s[i] == "V":
                if i > 0 and s[i - 1] == "I":
                    sum -= 2
                sum += 5
            if s[i] == "I":
                sum += 1
            i += 1


        return sum
                
