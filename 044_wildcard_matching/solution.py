from typing import Dict, Tuple

"""
    Implement wildcard pattern matching with support for '?' and '*'.

    '?' Matches any single character.
    '*' Matches any sequence of characters (including the empty sequence).

    The matching should cover the entire input string (not partial).

    The function prototype should be:
    bool isMatch(const char *s, const char *p)

    Some examples:
    isMatch("aa","a") → false
    isMatch("aa","aa") → true
    isMatch("aaa","aa") → false
    isMatch("aa", "*") → true
    isMatch("aa", "a*") → true
    isMatch("ab", "?*") → true
    isMatch("aab", "c*a*b") → false

"""

class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        return self.is_match(s, 0, p, 0, {})

    def is_match(self, text: str, idx_text: int, pattern: str, idx_pattern: int, memo : Dict[Tuple[int, int], bool]):
        if len(pattern) == idx_pattern:
            return len(text) == idx_text

        if len(text) == idx_text:
            if pattern[idx_pattern] == '*':
                if (idx_text, idx_pattern + 1) not in memo:
                    memo[(idx_text, idx_pattern + 1)] = self.is_match(text, idx_text, pattern, idx_pattern + 1, memo)

                return memo[(idx_text, idx_pattern + 1)]
            else:
                return False

        if pattern[idx_pattern] == '?':
            if (idx_text + 1, idx_pattern + 1) not in memo:
                memo[(idx_text + 1, idx_pattern + 1)] = \
                    self.is_match(text, idx_text + 1, pattern, idx_pattern + 1, memo)
            return memo[(idx_text + 1, idx_pattern + 1)]
        elif pattern[idx_pattern] == '*':
            if (idx_text + 1, idx_pattern) not in memo:
                memo[(idx_text + 1, idx_pattern)] = self.is_match(text, idx_text + 1, pattern, idx_pattern, memo)
            if (idx_text, idx_pattern + 1) not in memo:
                memo[(idx_text, idx_pattern + 1)] = self.is_match(text, idx_text, pattern, idx_pattern + 1, memo)

            return memo[(idx_text + 1, idx_pattern)] or memo[(idx_text, idx_pattern + 1)]
        else:
            if pattern[idx_pattern] == text[idx_text]:
                if (idx_text + 1, idx_pattern + 1) not in memo:
                    memo[(idx_text + 1, idx_pattern + 1)] = self.is_match(text, idx_text + 1, pattern, idx_pattern + 1, memo)
                return memo[(idx_text + 1, idx_pattern + 1)]
            else:
                return False

    def is_match_slow(self, text : str, idx_text : int, pattern : str, idx_pattern : int):
        if len(pattern) == idx_pattern:
            return len(text) == idx_text

        if len(text) == idx_text:
            return pattern[idx_pattern] == '*' and self.is_match_slow(text, idx_text, pattern, idx_pattern+1)

        if pattern[idx_pattern] == '?':
            return self.is_match_slow(text, idx_text + 1, pattern, idx_pattern + 1)
        elif pattern[idx_pattern] == '*':
            return self.is_match_slow(text, idx_text + 1, pattern, idx_pattern) or \
                   self.is_match_slow(text, idx_text, pattern, idx_pattern + 1)
        else:
            return pattern[idx_pattern] == text[idx_text] \
                   and self.is_match_slow(text, idx_text + 1, pattern, idx_pattern + 1)

if __name__ == '__main__':
    test = Solution()
    print(test.isMatch("aa", "a")) # false
    print(test.isMatch("aa", "aa")) # true
    print(test.isMatch("aaa", "aa")) # false
    print(test.isMatch("aa", "*")) # true
    print(test.isMatch("aa", "a*")) # true
    print(test.isMatch("ab", "?*")) # true
    print(test.isMatch("aab", "c*a*b")) # false