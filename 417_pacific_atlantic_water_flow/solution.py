from typing import List, Tuple, Set
from queue import Queue

class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])
        if n == 0:
            return []

        def get_neighbor(t: Tuple[int, int]) -> List[Tuple[int, int]]:
            x, y = t
            neighbors = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
            result = [(i, j) for i, j in neighbors if i >= 0 and i < m and j >= 0 and j < n]
            return result


        def BFS(ocean: Set[Tuple[int, int]]):
            queue = Queue()
            for point in ocean:
                queue.put(point)
            while queue.qsize() > 0:
                current = queue.get()
                neighbors = get_neighbor(current)
                for neighbor in neighbors:
                    if neighbor not in ocean and matrix[neighbor[0]][neighbor[1]] >= matrix[current[0]][current[1]]:
                        queue.put(neighbor)
                        ocean.add(neighbor)

        pacific = set()
        for i in range(n):
            pacific.add((0, i))
        for i in range(1, m):
            pacific.add((i, 0))
        BFS(pacific)

        atlantic = set()
        for i in range(n):
            atlantic.add((m - 1, i))
        for i in range(m - 1):
            atlantic.add((i, n - 1))
        BFS(atlantic)

        return list(map(lambda t: [t[0], t[1]], pacific.intersection(atlantic)))



if __name__ == '__main__':
    matrix = [[1, 2, 2, 3, 5],
              [3, 2, 3, 4, 4],
              [2, 4, 5, 3, 1],
              [6, 7, 1, 4, 5],
              [5, 1, 1, 2, 4]]
    test = Solution()
    print(test.pacificAtlantic(matrix))


