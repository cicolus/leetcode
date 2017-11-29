from typing import List

class Solution: # TODO
    def maximalRectangle(self, matrix : List[List[str]]) -> int:
        if not matrix:
            return 0

        height = len(matrix)
        width = len(matrix[0])

        if width == 0:
            return 0

        dp = [[(0, 0)] * width for _ in range(height)] # (height, width)
        for i in range(height):
            for j in range(width):
                if i == 0: # in first row
                    if matrix[i][j] == '1':
                        dp[i][j] = (1, 1)
                elif j == 0: # i > 0, j == 0, in first column
                    if matrix[i][j] == '1':
                        dp[i][j] = (1 + dp[i - 1][j][0], 1)
                elif matrix[i][j] == '1': # in rest of the matrix
                    if matrix[i-1][j] == '0':
                        dp[i][j] = (1, 1 + dp[i][j - 1][1])
                    elif matrix[i][j-1] == '0':
                        dp[i][j] = (1 + dp[i-1][j][0], 1)
                    elif matrix[i-1][j-1] == '0':
                        """
                            TODO
                        """



if __name__ == '__main__':
    test = Solution()
    matrix_1 = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"],
                ["1", "0", "0", "1", "0"]]
    print(test.maximalRectangle(matrix_1))