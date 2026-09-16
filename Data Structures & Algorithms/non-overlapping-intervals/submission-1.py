class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        counter = 0

        intervals.sort()
        prev_high = intervals[0][1]

        for start, end in intervals[1:]:
            if start < prev_high:
                counter += 1
                prev_high = min(prev_high, end)
            else:
                prev_high = end
        return counter
