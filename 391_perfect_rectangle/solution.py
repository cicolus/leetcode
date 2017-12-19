from typing import List, Tuple, Dict
from math import inf

class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        vertices = {} # type: Dict[Tuple[int, int], int]
        # lower left   :  0001
        # lower right  :  0010
        # upper right  :  0100
        # upper left   :  1000
        area_sum = 0
        lower_left, highest_right = (inf, inf), (-inf, -inf)
        def check_bit(vertex, bit_pattern):
            nonlocal vertices
            if vertex in vertices:
                if vertices[vertex] & bit_pattern > 0:
                    return False
                else:
                    vertices[vertex] = vertices[vertex] | bit_pattern
            else:
                vertices[vertex] = bit_pattern

            return True

        for lo_x, lo_y, hi_x, hi_y in rectangles:
            lo_left, lo_right = (lo_x, lo_y), (hi_x, lo_y)
            up_left, up_right = (lo_x, hi_y), (hi_x, hi_y)
            lower_left = min(lower_left, lo_left)
            highest_right = max(highest_right, up_right)
            area_sum += (hi_x - lo_x) * (hi_y - lo_y)
            if not check_bit(lo_left, 0x1): return False
            if not check_bit(lo_right, 0x2): return False
            if not check_bit(up_right, 0x4): return False
            if not check_bit(up_left, 0x8): return False

        count = 0
        if area_sum != (highest_right[0] - lower_left[0]) * (highest_right[1] - lower_left[1]): return False
        for vertex in vertices:
            if vertices[vertex] in [0x1, 0x2, 0x4, 0x8]:
                count += 1
        if count != 4:
            return False
        return True

if __name__ == '__main__':
    test = Solution()
    print(test.isRectangleCover([
        [1, 1, 3, 3],
        [3, 1, 4, 2],
        [3, 2, 4, 4],
        [1, 3, 2, 4],
        [2, 3, 3, 4]
    ]))  # True
    print(test.isRectangleCover([
        [1, 1, 2, 3],
        [1, 3, 2, 4],
        [3, 1, 4, 2],
        [3, 2, 4, 4]
    ])) # False
    print(test.isRectangleCover([
        [1, 1, 3, 3],
        [3, 1, 4, 2],
        [1, 3, 2, 4],
        [3, 2, 4, 4]
    ])) # False
    print(test.isRectangleCover([
        [1, 1, 3, 3],
        [3, 1, 4, 2],
        [1, 3, 2, 4],
        [2, 2, 4, 4]
    ])) # False
    print(test.isRectangleCover([
        [0, 0, 1, 1],
        [0, 2, 1, 3],
        [1, 1, 2, 2],
        [2, 0, 3, 1],
        [2, 2, 3, 3],
        [1, 0, 2, 3],
        [0, 1, 3, 2]
    ])) # False

