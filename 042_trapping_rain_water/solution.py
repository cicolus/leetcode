from typing import List

class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) == 0:
            return 0

        left_max = [height[0]]
        right_max = [height[-1]]
        for i in range(1, len(height)):
            left_max.append(max(left_max[i-1], height[i]))
            right_max.append(max(right_max[i-1], height[-1-i]))

        right_max = list(reversed(right_max))

        rain = 0

        for i in range(len(height)):
            rain += min(right_max[i], left_max[i]) - height[i]

        return rain


if __name__ == '__main__':
    test = Solution()
    print(test.trap([0,1,0,2,1,0,1,3,2,1,2,1])) # 6