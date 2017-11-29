from typing import List, Tuple
from heapq import heappop, heappush

"""
    Given an array of meeting time intervals consisting of start and end times 
    [[s1,e1],[s2,e2],...] (si < ei), 
    find the minimum number of conference rooms required.
   
    For example,
    Given [[0, 30],[5, 10],[15, 20]],
    return 2.
"""


# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __repr__(self):
        return "[" + str(self.start) + ", " + str(self.end) + "]"

class Solution:
    def minMeetingRooms(self, intervals : List[Interval]):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals:
            return 0
        intervals = sorted(list(map(lambda x : (x.start, x.end), intervals)))
        assignments = [(intervals[0][1], [intervals[0]])] # type: List[Tuple[int, List[Interval]]]
        for i in range(1, len(intervals)):
            end, room_schedule = heappop(assignments) # type: int, List[Interval]
            if intervals[i][0] < end:
                heappush(assignments, (end, room_schedule))
                heappush(assignments, (intervals[i][1], [intervals[i]]))
            else:
                room_schedule.append(intervals[i])
                heappush(assignments, (intervals[i][1], room_schedule))

        return len(assignments)


if __name__ == '__main__':
    test = Solution()
    intervals = [Interval(0, 30), Interval(5, 10), Interval(15, 20)]
    print(test.minMeetingRooms(intervals)) # 2
    print(test.minMeetingRooms([Interval(1, 17), Interval(7, 10), Interval(12, 14)])) # 2
    print(test.minMeetingRooms([Interval(1,4), Interval(1,5), Interval(2,9), Interval(2,6),
                                Interval(10,19), Interval(11,14), Interval(9,8)])) # 4
    print(test.minMeetingRooms([Interval(5,8), Interval(6, 8)])) # 2