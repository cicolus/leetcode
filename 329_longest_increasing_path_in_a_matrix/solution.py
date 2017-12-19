from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        n, m = len(matrix), len(matrix[0])
        dp = [[-1] * m for _ in range(n)]

        def get_neighbors(x, y):
            result = []
            for i, j in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                if 0 <= i and i < n and 0 <= j and j < m:
                    result.append((i, j))
            return result

        def DFS(x, y):
            if dp[x][y] != -1:
                return dp[x][y]
            dp[x][y] = 1
            neighbors = get_neighbors(x, y)
            for i, j in neighbors:
                if matrix[i][j] > matrix[x][y]:
                    dp[x][y] = max(dp[x][y], 1 + DFS(i, j))
            return dp[x][y]

        for i in range(n):
            for j in range(m):
                if dp[i][j] < 0:
                    DFS(i, j)
        return max(map(max, dp))

if __name__ == '__main__':
    test = Solution()
    print(test.longestIncreasingPath([
        [9, 9, 4],
        [6, 6, 8],
        [2, 1, 1]
    ])) # 4
    print(test.longestIncreasingPath([
        [9, 10, 4],
        [6, 6, 8],
        [2, 1, 1]
    ])) # 5
    print(test.longestIncreasingPath([
        [3, 4, 5],
        [3, 2, 6],
        [2, 2, 1]
    ])) # 4
