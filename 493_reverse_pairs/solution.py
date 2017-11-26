from typing import List


class Solution:
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # TODO: implement divide and conquer solution

    def reverse_pairs_dc(self, nums, i, j):
        """
        :type nums: List[int]
        :type i: int
        :type j: int
        :rtype: int
        """
        if i >= j:
            return 0
        mid = (i+j) // 2
