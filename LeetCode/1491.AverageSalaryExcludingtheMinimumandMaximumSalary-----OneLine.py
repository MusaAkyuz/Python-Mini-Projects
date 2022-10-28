class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """

        """
        Mission
        You are given an array of unique integers salary where salary[i] is the salary of the ith employee.
        Return the average salary of employees excluding the minimum and maximum salary. 
        Answers within 10-5 of the actual answer will be accepted.
        """

        return float((sum(salary) - min(salary) - max(salary))) / (len(salary) - 2)