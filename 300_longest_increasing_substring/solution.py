from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp = [0] * len(nums)
        for i in range(len(nums)):
            curr = 1
            for j in range(i):
                if nums[i] > nums[j]:
                    curr = max(curr, 1 + dp[j])
            dp[i] = curr
        return max(dp)

if __name__ == '__main__':
    test = Solution()
    print(test.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])) # 4
    print(test.lengthOfLIS([1, 3, 6, 7, 9, 4, 10, 5, 6])) # 6
