class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        """
        Given an array of strings strs, group the anagrams together. You can return the answer in any order.

        An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
        typically using all the original letters exactly once.
        """

        # creating frequency for group
        # it is same value for every group
        def frequency(lis):
            uniq = set(lis)
            freq = {}
            for i in uniq:
                freq[i] = lis.count(i)
            return freq

        i = 0
        count = 0
        types = []
        res = [[] for _ in xrange(len(strs))]
        while i < len(strs):
            type1 = frequency(strs[i])
            if type1 not in types:
                res[count].append(strs[i])
                count += 1
                types.append(type1)
            else:
                res[types.index(type1)].append(strs[i])
                res.pop()
            i += 1

        return res
        