from typing import List
from heapq import heappop, heappush

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses = list(sorted(courses, key=lambda t: t[1]))
        heap = []
        total_time = 0
        for length, deadline in courses:
            total_time += length
            heappush(heap, -length)
            if total_time > deadline:
                to_delete = heappop(heap)
                total_time += to_delete
        return len(heap)

if __name__ == '__main__':
    test = Solution()
    print(test.scheduleCourse([[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]))