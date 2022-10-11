class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        '''
        Mission
        You are a product manager and currently leading a team to develop a new product. 
        Unfortunately, the latest version of your product fails the quality check. 
        Since each version is developed based on the previous version, all the versions after a 
        bad version are also bad.

        Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes 
        all the following ones to be bad.

        You are given an API bool isBadVersion(version) which returns whether version is bad. 
        Implement a function to find the first bad version. You should minimize the number of calls to the API
        '''

        # Cant use linear search algorithm

        # for version in range(n):
        #     if isBadVersion(version + 1):
        #         return version + 1

        # BINARY SEARCH

        # 1 to n
        low, high = 1, n

        while low < high:
            # changes middle every time according to value
        	mid = (low + high) // 2

            # if value is false we should write new low 
        	if not isBadVersion(mid):
        		low = mid + 1
        	# if value is true we should write new high
            else:
        		high = mid
        # last thing high equals the solution
        return high
