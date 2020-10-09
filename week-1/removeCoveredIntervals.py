class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        ans = 0
        intervals.sort(key = lambda x : (x[0], -x[1]))
        endTime = -1
        for i in intervals:
            if i[1]<=endTime:
                ans += 1
            else:
                endTime = i[1]
        return len(intervals) - ans