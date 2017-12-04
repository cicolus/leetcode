from typing import List


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> [List[List[int]]]:
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """

        def helper(lo: int, hi: int) -> List[List[int]]:
            if hi - lo == 1:
                return [[buildings[lo][0], buildings[lo][2]], [buildings[lo][1], 0]]
            else:
                mid = (lo + hi) // 2
                left = helper(lo, mid)
                right = helper(mid, hi)
                merged = []
                ptr_left, ptr_right = 0, 0
                height_left, height_right = 0, 0
                while ptr_left < len(left) and ptr_right < len(right):
                    if left[ptr_left][0] < right[ptr_right][0]:
                        height_left = left[ptr_left][1]
                        merged.append([left[ptr_left][0], max(height_left, height_right)])
                        ptr_left += 1
                    elif left[ptr_left][0] > right[ptr_right][0]:
                        height_right = right[ptr_right][1]
                        merged.append([right[ptr_right][0], max(height_left, height_right)])
                        ptr_right += 1
                    else:
                        height_left = left[ptr_left][1]
                        height_right = right[ptr_right][1]
                        merged.append([left[ptr_left][0], max(height_left, height_right)])
                        ptr_left += 1
                        ptr_right += 1
                if ptr_left < len(left):
                    merged.extend(left[ptr_left:])
                if ptr_right < len(right):
                    merged.extend(right[ptr_right:])
                return merged

        if not buildings:
            return []
        result = helper(0, len(buildings))
        consolidated = []
        i = 0
        while i < len(result):
            if not (consolidated and result[i][1] == consolidated[-1][1]):
                consolidated.append(result[i])
            i += 1
        return consolidated


if __name__ == '__main__':
    test = Solution()
    print(test.getSkyline([[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]))
    # [[2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0]]
    print(test.getSkyline([[2, 9, 10]]))
    # [[2, 10], [9, 0]]
    print(test.getSkyline([[1, 5, 11], [2, 7, 6], [3, 9, 13], [12, 16, 7],
                           [14, 25, 3], [19, 22, 18], [23, 29, 13], [24, 28, 4]]))
    # [1, 11], [3, 13], [9, 0], [12, 7], [14, 3], [19, 18], [22, 3], [23, 13], [29, 0]
    print(test.getSkyline([[2, 9, 10], [9, 12, 15]]))
    # [[2, 10], [9, 15], [12, 0]]
