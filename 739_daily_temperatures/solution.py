from typing import List

"""
    739. Daily Temperatures
    
    Given a list of daily temperatures, produce a list that, for each 
    day in the input, tells you how many days you would have to wait until 
    a warmer temperature. If there is no future day for which this is possible, 
    put 0 instead.

    For example, given the list temperatures = [73, 74, 75, 71, 69, 72, 76, 73], 
    your output should be [1, 1, 4, 2, 1, 1, 0, 0].

    Note: The length of temperatures will be in the range [1, 30000]. 
    Each temperature will be an integer in the range [30, 100].
"""

class Solution:
    def dailyTemperatures(self, temperatures : List[int]) -> List[int]:
        size = len(temperatures)
        ret = [0] * size
        stack = []
        idx = 0
        while idx < size:
            if not stack:
                stack.append(idx)
                idx += 1
            else:
                if temperatures[stack[-1]] < temperatures[idx]:
                    ret[stack[-1]] = idx - stack[-1]
                    stack.pop()
                else:
                    stack.append(idx)
                    idx += 1

        return ret



if __name__ == '__main__':
    test = Solution()
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    print(test.dailyTemperatures(temperatures))
