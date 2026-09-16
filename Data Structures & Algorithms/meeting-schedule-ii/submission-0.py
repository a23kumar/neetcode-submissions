"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([val.start for val in intervals])
        end = sorted([val.end for val in intervals])

        rooms = 0
        res = 0
        i = 0
        j = 0
        while i < len(start):
            if start[i] < end[j]:
                rooms += 1
                res = max(res, rooms)
                i += 1
            else:
                rooms -= 1
                j += 1
        
        return res