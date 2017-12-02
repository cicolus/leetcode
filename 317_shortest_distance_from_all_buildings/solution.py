from pprint import pprint
from typing import List
from queue import Queue
from math import inf, isinf

"""
    You want to build a house on an empty land which reaches all buildings in the shortest amount of distance. 
    You can only move up, down, left and right. You are given a 2D grid of values 0, 1 or 2, where:

    - Each 0 marks an empty land which you can pass by freely.
    - Each 1 marks a building which you cannot pass through.
    - Each 2 marks an obstacle which you cannot pass through.
    
    For example, given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2):
    
    1 - 0 - 2 - 0 - 1
    |   |   |   |   |
    0 - 0 - 0 - 0 - 0
    |   |   |   |   |
    0 - 0 - 1 - 0 - 0
    
    The point (1,2) is an ideal empty land to build a house, as the total travel distance of 3+3+1=7 is minimal. 
    So return 7.
    
    Note:
    There will be at least one building. If it is not possible to build such house according to the above rules, 
    return -1.
    
"""

class Solution:
    def shortestDistance(self, grid : List[List[int]]) -> int:
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return -1

        height = len(grid)
        width = len(grid[0])

        min_dist = [[0] * width for _ in range(height)]
        reachable = [[True] * width for _ in range(height)]
        for i in range(height):
            for j in range(width):
                if grid[i][j] == 1:
                    visited = [[False] * width for _ in range(height)]
                    q = Queue()
                    q.put((i, j, 0))
                    visited[i][j] = True
                    while q.qsize() > 0:
                        next_i, next_j, step = q.get()
                        min_dist[next_i][next_j] += step
                        neighbors = [(next_i - 1, next_j), (next_i + 1, next_j),
                                     (next_i, next_j - 1), (next_i, next_j + 1)]
                        for x, y in neighbors:
                            if x < height and x >= 0 and y < width and y >= 0:
                                if grid[x][y] == 0 and not visited[x][y]:
                                    q.put((x, y, step + 1))
                                    visited[x][y] = True
                                elif grid[x][y] == 1 and not visited[x][y] and grid[next_i][next_j] != 1:
                                    visited[x][y] = True
                                    min_dist[x][y] += step + 1
                    for n in range(height):
                        for m in range(width):
                            if grid[n][m] == 1 and not visited[n][m]:
                                return -1
                            if grid[n][m] == 0 and not visited[n][m]:
                                reachable[n][m] = False
                    # pprint(visited)
        # pprint(min_dist)
        ret = inf
        for i in range(height):
            for j in range(width):
                if grid[i][j] == 0 and min_dist[i][j] != 0 and reachable[i][j]:
                    ret = min(ret, min_dist[i][j])

        if isinf(ret):
            return -1
        return ret


if __name__ == '__main__':
    test = Solution()
    grid_1 = [[1, 0, 2, 0, 1],
              [0, 0, 0, 0, 0],
              [0, 0, 1, 0, 0]]
    print(test.shortestDistance(grid_1)) # 7
    grid_2 = [[1, 0, 2, 0, 1],
              [1, 0, 2, 0, 0],
              [1, 0, 2, 0, 0]]
    print(test.shortestDistance(grid_2)) # -1
    grid_3 = [[1, 0, 0, 2, 0],
              [0, 1, 0, 2, 0],
              [0, 0, 1, 2, 0]]
    print(test.shortestDistance(grid_3)) # 5
    grid_4 = [[1, 1],
              [0, 1]]
    print(test.shortestDistance(grid_4)) # -1
    grid_5 = [[0, 0, 0, 0],
              [1, 1, 1, 0],
              [1, 1, 1, 0],
              [0, 1, 1, 0]]
    print(test.shortestDistance(grid_5)) # -1
    grid_6 = [[1, 1, 1, 1, 1, 0],
              [0, 0, 0, 0, 0, 1],
              [0, 1, 1, 0, 0, 1],
              [1, 0, 0, 1, 0, 1],
              [1, 0, 1, 0, 0, 1],
              [1, 0, 0, 0, 0, 1],
              [0, 1, 1, 1, 1, 0]]
    print(test.shortestDistance(grid_6)) # 88
