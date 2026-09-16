class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        res = []

        for i, interval in enumerate(intervals):
            # 1. newInterval comes completely before the current interval
            if newInterval[1] < interval[0]:
                res.append(newInterval)
                return res + intervals[i:]

            # 2. newInterval comes completely after the current interval
            elif newInterval[0] > interval[1]:
                res.append(interval)

            # 3. Overlap detected: expand newInterval to encompass both
            else:
                newInterval = [
                    min(newInterval[0], interval[0]),
                    max(newInterval[1], interval[1]),
                ]

        # If newInterval was never added (it belongs at the very end)
        res.append(newInterval)
        return res