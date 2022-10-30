class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        """
        Mission
        Given an integer n, return a string array answer (1-indexed) where:

        answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
        answer[i] == "Fizz" if i is divisible by 3.
        answer[i] == "Buzz" if i is divisible by 5.
        answer[i] == i (as a string) if none of the above conditions are true.
        """
        
        res = []
        i = 1

        while i <= n:
            if i%15 == 0:
                res.append("FizzBuzz")
            elif i%5 == 0:
                res.append("Buzz")
            elif i%3 == 0:
                res.append("Fizz")
            else:
                res.append(str(i))
            i += 1
        return res