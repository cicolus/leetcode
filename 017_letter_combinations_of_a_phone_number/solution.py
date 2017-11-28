from typing import List

class Solution:
    def __init__(self):
        self.two = ['a', 'b', 'c']
        self.three = ['d', 'e', 'f']
        self.four = ['g', 'h', 'i']
        self.five = ['j', 'k', 'l']
        self.six = ['m', 'n', 'o']
        self.seven = ['p', 'q', 'r', 's']
        self.eight = ['t', 'u', 'v']
        self.nine = ['w', 'x', 'y', 'z']
        self.offset_table = [None, None, self.two, self.three,
                             self.four, self.five, self.six,
                             self.seven, self.eight, self.nine] # type: List[List[str]]


    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        if not filter(lambda c : c == '1' or c == '0', list(digits)):
            return []


        ret_lst = []
        for c in digits:
            letters = self.offset_table[int(c)]
            if not ret_lst:
                ret_lst.extend(letters)
            else:
                ret_lst = [s+l for s in ret_lst for l in letters]
        return  ret_lst






if __name__ == '__main__':
    test = Solution()
    print(test.letterCombinations("23"))
    # ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]