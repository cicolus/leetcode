from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        buys = [0] * len(prices)
        sells = [0] * len(prices)
        buys[0] = -prices[0]
        for i in range(1, len(prices)):
            sells[i] = max(sells[i-1], prices[i] + buys[i-1])
            buys[i] = max(buys[i-1], sells[i-2] - prices[i])
        return sells[-1]

if __name__ == '__main__':
    test = Solution()
    print(test.maxProfit([1, 2, 3, 0, 2]))
    print(test.maxProfit([1]))
    print(test.maxProfit([3]))
    print(test.maxProfit([1, 3]))
    print(test.maxProfit([1, 7, 9, 0, 10]))
