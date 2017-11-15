from typing import Dict

def match_without_kleene(text, pattern):
    if text and pattern:
        return (pattern[0] == text[0] or pattern[0] == '.') \
                and match_without_kleene(text[1:],pattern[1:])
    return not text and not pattern

def match_recursive(text, pattern):
    pass

def isMatch(text, pattern):
    if not pattern:
        return not text

    first_match = bool(text) and pattern[0] in {text[0], '.'}

    if len(pattern) >= 2 and pattern[1] == '*':
        return (isMatch(text, pattern[2:]) or
                first_match and isMatch(text[1:], pattern))
    else:
        return first_match and isMatch(text[1:], pattern[1:])


"""
    Submission code is the class below
"""

class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        memo = {}
        return self._is_match(s, 0, p, 0, memo)


    def _is_match(self, text, i, pattern, j, memo):
        """
        :type text: str
        :type i: int
        :type pattern: str
        :type j: int
        :type memo: Dict[(int, int), bool]
        :rtype: bool
        """
        if j == len(pattern):
            return i == len(text)

        if len(pattern) > j+1 and pattern[j+1] == '*':
            if i == len(text):
                if (i, j+2) not in memo:
                    memo[(i, j + 2)] = self._is_match(text, i, pattern, j + 2, memo)
                return memo[(i, j+2)]
            if text[i] == pattern[j] or pattern[j] == '.':
                if (i+1, j) not in memo:
                    memo[(i+1, j)] = self._is_match(text, i+1, pattern, j, memo)
                if (i, j+2) not in memo:
                    memo[(i, j+2)] = self._is_match(text, i, pattern, j+2, memo)
                return memo[(i + 1, j)] or memo[(i, j + 2)]
            if (i, j+2) not in memo:
                memo[(i, j+2)] = self._is_match(text, i, pattern, j+2, memo)
            return memo[(i, j+2)]
        else: # next not Kleene star
            if i == len(text):
                return False
            if (text[i] == pattern[j] or pattern[j] == '.'):
                if (i+1, j+1) not in memo:
                    memo[(i+1, j+1)] = self._is_match(text, i+1, pattern, j+1, memo)
                return memo[(i+1, j+1)]
            return False

    def _is_match_slow(self, text, i, pattern, j):
        if j == len(pattern):
            return i == len(text)

        if len(pattern) > j+1 and pattern[j+1] == '*':
            if i == len(text):
                return self._is_match_slow(text, i, pattern, j+2)
            if text[i] == pattern[j] or pattern[j] == '.':
                return self._is_match_slow(text, i+1, pattern, j) or self._is_match_slow(text, i, pattern, j+2)
            return self._is_match_slow(text, i, pattern, j+2)
        else:
            if i == len(text):
                return False
            if (text[i] == pattern[j] or pattern[j] == '.'):
                return self._is_match_slow(text, i+1, pattern, j+1)
            return False


if __name__ == '__main__':
    test = Solution()
    print(test.isMatch("aaaab", ".*b")) # true
    print(test.isMatch("aaccb", ".*b")) # true
    print(test.isMatch("aa", "a")) # false
    print(test.isMatch("aa", "aa")) # true
    print(test.isMatch("aaa", "aa")) # false
    print(test.isMatch("aa", "a*")) # true
    print(test.isMatch("aa", ".*")) # true
    print(test.isMatch("ab", ".*")) # true
    print(test.isMatch("aab", "c*a*b")) # true