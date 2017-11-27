from typing import List

class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '':
            return 0
        dp = [0] * len(s) # type: List[int]
        for idx in range(1, len(s)):
            if s[idx] == ')':
                if s[idx-1] == '(':
                    dp[idx] = 2 + dp[idx-2] if idx >= 2 else 2
                elif dp[idx-1] > 0 and idx - dp[idx-1] - 1 >= 0 \
                        and s[idx - dp[idx-1] - 1] == '(':
                    dp[idx] = dp[idx-1] + 2
                    if idx - dp[idx-1] - 1 > 0:
                        dp[idx] += dp[idx - dp[idx - 1] - 2]
        return max(dp)


if  __name__ == '__main__':
    test = Solution()
    print(test.longestValidParentheses("(()")) # 2
    print(test.longestValidParentheses(")()())")) # 4
    print(test.longestValidParentheses("(()))())(")) # 4
    print(test.longestValidParentheses("(((()())())(()")) # 10
    print(test.longestValidParentheses("(((()())())())")) # 14
    print(test.longestValidParentheses("()(())((()")) # 6
    print(test.longestValidParentheses("((()())()))))((()(())))()()()(()))()())")) # 20