from typing import List

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
        intervals = sorted(intervals, key=lambda x : x.start)
        print(intervals)


if __name__ == '__main__':
    test = Solution()
    intervals = [Interval(0, 30), Interval(5, 10), Interval(15, 20)]
    print(test.minMeetingRooms(intervals))