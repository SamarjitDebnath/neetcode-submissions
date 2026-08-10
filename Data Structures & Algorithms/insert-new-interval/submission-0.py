class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for interval in intervals:
            iStart, iEnd = interval
            nStart, nEnd = newInterval

            if iStart > nEnd:
                res.append(newInterval)
                newInterval = interval
            elif nStart > iEnd:
                res.append(interval)
            else:
                nStart = min(iStart, nStart)
                nEnd = max(iEnd, nEnd)
                newInterval = [nStart, nEnd]

        res.append(newInterval)
        return res