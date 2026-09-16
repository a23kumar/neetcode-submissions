"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i: i.start)
        for i in range(1, len(intervals)):
            i_start = intervals[i].start
            i_end_prev = intervals[i - 1].end
            if i_start < i_end_prev:
                return False

        return True
    