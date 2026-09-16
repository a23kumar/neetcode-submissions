class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()
        # [[1,3],[1,5],[6,7]]
        low = intervals[0][0]
        high = intervals[0][1]
        temp = []
        for item in intervals[1:]:
            start = item[0] # 1
            end = item[1] # 5
            if start > high:
                res.append([low, high])
                low = start
                high = end
            else:
                high = max(high, end)


        res.append([low, high])
        return res