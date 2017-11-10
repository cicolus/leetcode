class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(t) > len(s):
            return ''

        remains = {}
        targets = {}
        for c in t:
            if c in remains:
                remains[c] += 1
                targets[c] += 1
            else:
                remains[c] = 1
                targets[c] = 1

        min_len = -1
        min_indices = (-1, -1)

        left = 0
        right = 0
        size = len(s)

        condition = True
        counter = {} # dictionary count the occurrences of chars in the current window
        while right < size:

            while remains and right < size:
                c = s[right]
                if c in targets:
                    if c in counter:
                        counter[c] += 1
                    else:
                        counter[c] = 1
                    if c in remains:
                        if remains[c] > 1:
                            remains[c] -= 1
                        else:
                            remains.pop(c)
                right += 1

            if right == size and remains :
                break

            def check(c):
                if c in targets:
                    return counter[c] > targets[c]
                else:
                    return True

            while check(s[left]):
                if s[left] in targets:
                    counter[s[left]] -= 1
                left += 1

            if right - left < min_len or min_len == -1:
                min_len = right - left
                min_indices = (left, right)

            counter[s[left]] -= 1
            remains[s[left]] = 1
            if counter[s[left]] == 0:
                counter.pop(s[left])
            left += 1

        if min_len > 0:
            return s[min_indices[0]:min_indices[1]]
        else:
            return ''


if __name__ == '__main__':
    test = Solution()
    print(test.minWindow("adobecodebanc", "abc"))