class Solution(object):
    def earliestFullBloom(self, plantTime, growTime):
        """
        :type plantTime: List[int]
        :type growTime: List[int]
        :rtype: int
        """

        # first of all
        # we have to find max growing time plant
        # because we can save the time with use growing and planting same time
        # every time we will look longer growing time and adding
    
        # https://github.com/masanbasa3k/
        times = list(zip(plantTime, growTime))
        times.sort(key = lambda x: -x[1])

        first = list(times[0])
        lastAdd = first[1]
        res = first[0]
        for plant, grow in times[1:]:
            res += plant
            if lastAdd > plant + grow:
                lastAdd = lastAdd - plant
            else:
                lastAdd = grow

        return res + lastAdd