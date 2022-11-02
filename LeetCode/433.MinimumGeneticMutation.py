import copy

class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """

        """
        Mission
        A gene string can be represented by an 8-character long string, with choices 
        from 'A', 'C', 'G', and 'T'.

        Suppose we need to investigate a mutation from a gene string start to a 
        gene string end where one mutation is defined as one single character changed 
        in the gene string.

        For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
        There is also a gene bank bank that records all the valid gene mutations. 
        A gene must be in bank to make it a valid gene string.

        Given the two gene strings start and end and the gene bank bank, return the 
        minimum number of mutations needed to mutate from start to end. If there is no 
        such a mutation, return -1.

        Note that the starting point is assumed to be valid, so it might not be included 
        in the bank.
        """

        def checkOneDiff (gen1, gen2):
            count = 0
            for i in range(len(gen1)):
                if gen1[i] != gen2[i]:
                    count += 1
            return count == 1 # true or false

        deque = []
        deque.append(start)
        deque.append(0)
        # first item is mutation
        # second item is step number
        visited = set()

        while deque:
            currGen = deque.pop(0)
            step = deque.pop(0)

            if currGen == end:
                return step

            for i in bank:
                if checkOneDiff(currGen, i) and i not in visited:
                    deque.append(i)
                    deque.append(step + 1)
                    visited.add(i)
        return -1



        



                

