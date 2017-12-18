from typing import List
from array import array

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        m = len(grid)
        n = len(grid[0])

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
            return map(lambda t: t[0] * n + t[1],
                       filter(lambda t: t[0] >= 0 and t[0] < m and t[1] >= 0 and t[1] < n,
                              [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]))


        count = 0
        for x in range(m):
            for y in range(n):
                if grid[x][y] == '1':
                    current = x * n + y
                    forest[current] = current
                    count += 1
                    neighbors = get_neighbors(x, y)
                    for neighbor in neighbors:
                        if forest[neighbor] != -1 and union(current, neighbor):
                            count -= 1
        return count

if __name__ == '__main__':
    test = Solution()
    print(test.numIslands([["1", "1", "1", "1", "0"],
                           ["1", "1", "0", "1", "0"],
                           ["1", "1", "0", "0", "0"],
                           ["0", "0", "0", "0", "0"]]))

    print(test.numIslands([["1", "1", "0", "1", "0"],
                           ["1", "1", "0", "1", "0"],
                           ["0", "0", "1", "0", "0"],
                           ["0", "0", "0", "0", "0"]]))

    print(test.numIslands([["1", "1", "0", "1", "0"],
                           ["1", "1", "0", "1", "0"],
                           ["0", "0", "1", "1", "0"],
                           ["0", "0", "1", "0", "0"],
                           ["0", "0", "0", "0", "0"]]))
