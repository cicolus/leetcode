from typing import List, Dict, Tuple, Set
from math import gcd

# Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution:
    def maxPoints(self, points : List[Point]):
        """
        :type points: List[Point]
        :rtype: int
        """
        distinct_points_set = {} # type: Dict[Tuple[int, int], int]
        for point in points:
            x, y = point.x, point.y
            if (x, y) in distinct_points_set:
                distinct_points_set[(x, y)] += 1
            else:
                distinct_points_set[(x, y)] = 1

        if len(distinct_points_set) <= 2:
            return len(points)

        distinct_points = list(distinct_points_set.keys()) # type: List[Tuple[int, int]]
        lines = {} # type: Dict[Tuple[int, int, int], Set[Tuple[int, int]]]
        for i in range(len(distinct_points)-1):
            x1, y1 = distinct_points[i][0], distinct_points[i][1]
            for j in range(i+1, len(distinct_points)):
                x2, y2 = distinct_points[j][0], distinct_points[j][1]
                a = y2 - y1
                b = x1 - x2
                c = y1 * x2 - y2 * x1
                # represent the line as ax + by + c = 0
                d = gcd(gcd(a, b), c)
                line = (a//d, b//d, c//d)
                if line in lines:
                    lines[line].add((x1, y1))
                    lines[line].add((x2, y2))
                else:
                    lines[line] = {(x1, y1), (x2, y2)}

        def count(_line):
            return sum([distinct_points_set[x] for x in lines[_line]])

        max_line = max(lines.keys(), key=count)
        return count(max_line)

if __name__ == '__main__':
    test = Solution()
    print(test.maxPoints([]))
    print(test.maxPoints([Point(1, 2), Point(3, 4)]))
    print(test.maxPoints([Point(1, 2), Point(3, 4), Point(2, 4), Point(3, 6)]))