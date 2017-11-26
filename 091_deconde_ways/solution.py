from typing import Dict

class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '':
            return 0
        return self.num_decodings_dp(s, 0, {})

    def num_decoding(self, s : str, idx : int) -> int:
        if idx < len(s) - 1:
            if s[idx] == '0':
                return 0
            elif s[idx + 1] == '0':
                if int(s[idx]) <= 2:
                    return self.num_decoding(s, idx+2)
                else:
                    return 0
            elif int(s[idx:idx+2]) <= 26:
                return self.num_decoding(s, idx+1) + self.num_decoding(s, idx+2)
            else:
                return self.num_decoding(s, idx+1)
        elif idx == len(s) - 1:
            if s[idx] == '0':
                return 0
            else:
                return 1
        else:
            return 1


    def num_decodings_dp(self, s : str, idx : int, memo : Dict[int, int]) -> int:
        if idx < len(s) - 1:
            if s[idx] == '0':
                return 0
            elif s[idx + 1] == '0':
                if int(s[idx]) <= 2:
                    if idx + 2 not in memo:
                        memo[idx+2] = self.num_decodings_dp(s, idx + 2, memo)
                    return memo[idx+2]
                else:
                    return 0
            elif int(s[idx:idx + 2]) <= 26:
                if idx + 1 not in memo:
                    memo[idx + 1] = self.num_decodings_dp(s, idx + 1, memo)
                if idx + 2 not in memo:
                    memo[idx + 2] = self.num_decodings_dp(s, idx + 2, memo)
                return memo[idx+1] + memo[idx+2]
            else:
                if idx + 1 not in memo:
                    memo[idx + 1] = self.num_decodings_dp(s, idx + 1, memo)
                return memo[idx + 1]
        elif idx == len(s) - 1:
            if s[idx] == '0':
                return 0
            else:
                return 1
        else:
            return 1

if __name__ == '__main__':
    test = Solution()
    print(test.numDecodings("")) # 0
    print(test.numDecodings("12")) # 2
    print(test.numDecodings("102")) # 1
    print(test.numDecodings("1020")) # 1
    print(test.numDecodings("123456789")) # 3
    print(test.numDecodings("678765434567887654323321234567898998754523212123456787654321234567876")) # 1300
    print(test.numDecodings("01")) # 0
    print(test.numDecodings("09")) # 0
    print(test.numDecodings("90")) # 0
    print(test.numDecodings("80")) # 0