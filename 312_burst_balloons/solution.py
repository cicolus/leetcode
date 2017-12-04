from typing import List
from pprint import pprint
from math import inf

class Solution:
    def maxCoins(self, nums : List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [1] + nums + [1]
        size = len(nums)
        dp = [[0] * size for _ in range(size)]
        for diff in range(size - 2):
            for i in range(1, size - diff - 1):
                j = i + diff
                for k in range(i, j + 1):
                    dp[i][j] = max(dp[i][j], dp[i][k - 1] + nums[k] * nums[i- 1] * nums[j + 1] + dp[k + 1][j])
        return dp[1][size - 2]


if __name__ == '__main__':
    test = Solution()
    print(test.maxCoins([3, 1, 5, 8])) # 167
    print(test.maxCoins([])) # 0
    print(test.maxCoins([1, 2, 3, 4, 5, 6, 7, 8])) # 912
    print(test.maxCoins([1, 2, 3, 4, 5, 6, 7, 8, 9])) # 1530
    print(test.maxCoins([0, 1, 2, 3, 4, 5, 6, 7, 8])) # 912