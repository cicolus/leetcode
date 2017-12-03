"""
    340. Longest Substring with At Most K Distinct Characters

    Given a string, find the length of the longest substring T that contains at
    most k distinct characters.

    For example, Given s = “eceba”,

    T is "ece" which its length is 3.
"""


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0:
            return 0
        counter = {}
        max_len = 0
        prev_idx = 0
        i = 0
        while i < len(s):
            if s[i] in counter:
                counter[s[i]] += 1
            elif len(counter) < k:
                counter[s[i]] = 1
            else:
                max_len = max(max_len, i - prev_idx)
                while counter[s[prev_idx]] > 1:
                    counter[s[prev_idx]] -= 1
                    prev_idx += 1
                counter.pop(s[prev_idx])
                prev_idx += 1
                counter[s[i]] = 1
            i += 1
        return max(max_len, i - prev_idx)


if __name__ == '__main__':
    test = Solution()
    print(test.lengthOfLongestSubstringKDistinct("eceba", 2))  # 3
    print(test.lengthOfLongestSubstringKDistinct("", 2))  # 0
    print(test.lengthOfLongestSubstringKDistinct("a", 2))  # 1
    print(test.lengthOfLongestSubstringKDistinct("aa", 2))  # 2
    print(test.lengthOfLongestSubstringKDistinct("aaaaaaaaaabbbbbbbbbbbbcccccccccccccccc"
                                                   "bbbbbbbbbbbbbaaaaaaaaaaaaaaaaaaaaa", 2))  # 41
    print(test.lengthOfLongestSubstringKDistinct("a", 0))


