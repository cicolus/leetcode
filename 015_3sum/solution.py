from typing import List, Dict, Set, Tuple

class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        solutions = set()
        for idx in range(len(nums)):
            solutions = solutions.union(self.two_sum(nums, idx, -nums[idx]))

        return list(map(list, solutions))

    def two_sum(self, nums, skip_index, target):
        """
        :type nums: List[int]
        :type skip_index: int
        :type sum: int
        :rtype: Set[Tuple(int, int, int)]
        """
        solutions = set()
        complement = {} # type: Dict[int, int]
        for i in range(len(nums)):
            if i != skip_index:
                if nums[i] in complement:
                    solutions.add(tuple(sorted([nums[skip_index], complement[nums[i]], nums[i]])))
                else:
                    complement[target - nums[i]] = nums[i]

        return solutions




if __name__ == '__main__':
    test = Solution()
    test.threeSum([-1, 0, 1, 2, -1, -4])
    print(test.two_sum([-1, 0, 1, 2, -1, -4], 0, 1))