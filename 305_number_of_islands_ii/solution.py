from typing import List
from array import array

class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        forest = array('i', [-1] * (m * n))

        def union(x, y):
            set_x, set_y = find(x), find(y)
            if set_x == set_y:
                return False
            else:
                forest[set_x] = forest[set_y]
                return True

        def find(x):
            if forest[x] != x:
                forest[x] = find(forest[x])
            return forest[x]

        def get_neighbors(x, y):
            return map(lambda t: t[0]*n+t[1],
                       filter(lambda t: t[0] >= 0 and t[0] < m and t[1] >= 0 and t[1] < n,
                              [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]))

        count = 0
        result = []

        for x, y in positions:
            current = x * n + y
            forest[current] = current
            count += 1
            neighbors = get_neighbors(x, y)
            for neighbor in neighbors:
                if forest[neighbor] != -1 and union(current, neighbor):
                    count -= 1
            result.append(count)
        return result

if __name__ == '__main__':
    test = Solution()
    print(test.numIslands2(3, 3, [[0, 0], [0, 1], [1, 2], [2, 1]]))
    print(test.numIslands2(3, 3, [[0, 0], [0, 1], [1, 2], [2, 1], [0, 2]]))
    print(test.numIslands2(3, 3, [[0, 0], [0, 1], [1, 2], [2, 1], [0, 2], [2, 2]]))
    print(test.numIslands2(8, 2, [[7, 0]]))


