"""
    159. Longest Substring with At Most Two Distinct Characters

    Given a string, find the length of the longest substring T that contains at 
    most 2 distinct characters.

    For example, Given s = “eceba”,
    
    T is "ece" which its length is 3.
"""


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        counter = {}
        max_len = 0
        prev_idx = 0
        i = 0
        while i < len(s):
            if s[i] in counter:
                counter[s[i]] += 1
            elif len(counter) < 2:
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
    print(test.lengthOfLongestSubstringTwoDistinct("eceba")) # 3
    print(test.lengthOfLongestSubstringTwoDistinct("")) # 0
    print(test.lengthOfLongestSubstringTwoDistinct("a")) # 1
    print(test.lengthOfLongestSubstringTwoDistinct("aa"))  # 2
    print(test.lengthOfLongestSubstringTwoDistinct("aaaaaaaaaabbbbbbbbbbbbcccccccccccccccc"
                                                   "bbbbbbbbbbbbbaaaaaaaaaaaaaaaaaaaaa")) # 41


