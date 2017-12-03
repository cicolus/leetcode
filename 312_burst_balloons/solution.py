from typing import List
from math import inf

class Solution:
    def maxCoins(self, nums : List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        max_coin = -inf
        dp = [[0] * size for _ in range(size)]
        for diff in range(size):
            for i in range(size - diff):
                if diff == 0:
                    dp[i][i] = nums[i]
                else:
                    temp = [nums[i] * nums[i + 1] + dp[i + 1][i + diff]]
                    temp.append(nums[i + diff - 1] * nums[i + diff] + dp[i][i + diff - 1])
                    for k in range(i + 1, i + diff):
                        coin = nums[k] * nums[k - 1] * nums[k + 1] + dp[i][k - 1] + dp[k + 1][i + diff]
                        if k + 1 != i + diff and k - 1 != i:
                            coin -= nums[k + 1] * nums[k + 2] + nums[k - 1] * nums[k - 2]
                            coin += nums[k - 1] * nums[k + 1] * nums[k + 2] + nums[k - 2] * nums[k - 1] * nums[k + 1]
                        elif k + 1 != i + diff:
                            coin -= nums[k + 1] * nums[k + 2]
                            coin += nums[k - 1] * nums[k + 1] * nums[k + 2]
                        elif k - 1 != i:
                            coin -= nums[k - 1] * nums[k - 2]
                            coin += nums[k - 2] * nums[k - 1] * nums[k + 1]
                        else:
                            coin -= nums[k - 1] + nums[k + 1]
                            coin += nums[k - 1] * nums[k + 1]
                        temp.append(coin)
                    curr = max(temp)
                    dp[i][i + diff] = curr
                    if diff == size - 1:
                        max_coin = max(curr, max_coin)
        print(dp)
        return max_coin

if __name__ == '__main__':
    test = Solution()
    print(test.maxCoins([3, 1, 5, 8]))