from typing import Set

class Solution:
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def is_valid(s : str) -> bool:
            counter = 0
            for c in s:
                if c == '(':
                    counter += 1
                elif c == ')':
                    counter -= 1
                    if counter < 0:
                        return False
            return counter == 0

        curr = {s} # type: Set[str]
        while True:
            valid = list(filter(is_valid, curr))
            if valid:
                return valid
            new_curr = set()
            for curr_s in curr:
                for idx in range(len(curr_s)):
                    if curr_s[idx] == '(' or curr_s[idx] == ')':
                        new_curr.add(curr_s[:idx] + curr_s[idx+1:])
            curr = new_curr

if __name__ == '__main__':
    test = Solution()
    print(test.removeInvalidParentheses("()())()"))
    print(test.removeInvalidParentheses("(a)())()"))
    print(test.removeInvalidParentheses(")("))