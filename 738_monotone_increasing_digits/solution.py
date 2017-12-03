from typing import List

"""
    738. Monotone Increasing Digits

    Given a non-negative integer N, find the largest number that is less than 
    or equal to N with monotone increasing digits.

    (Recall that an integer has monotone increasing digits if and only if each 
    pair of adjacent digits x and y satisfy x <= y.)

    Example 1:
    
    Input: N = 10
    Output: 9
    
    Example 2:
    
    Input: N = 1234
    Output: 1234
    
    Example 3:
    Input: N = 332
    Output: 299
    
    Note: N is an integer in the range [0, 10^9].
"""

class Solution:
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        def is_monotone(m):
            while m > 0:
                if not (m % 10 >= (m // 10) % 10):
                    return False
                m //= 10
            return True

        if is_monotone(N):
            return N

        n_s = list(str(N))
        for i in range(len(n_s) - 1, -1, -1):
            if n_s[i] == '0':
                continue
            else:
                temp = n_s.copy()
                temp[i] = str(int(n_s[i]) - 1)
                for j in range(i + 1, len(temp)):
                    temp[j] = '9'
                temp = int(''.join(temp))
                if is_monotone(temp):
                    return temp





if __name__ == '__main__':
    test = Solution()
    print(test.monotoneIncreasingDigits(0))
    print(test.monotoneIncreasingDigits(10))
    print(test.monotoneIncreasingDigits(123))
    print(test.monotoneIncreasingDigits(332))
    print(test.monotoneIncreasingDigits(603253281))
    print(test.monotoneIncreasingDigits(668841))



