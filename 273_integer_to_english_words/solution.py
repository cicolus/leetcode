from typing import List

class Solution:

    def __init__(self):
        self.words = ["Zero", "One", "Two", "Three", "Four", "Five", "Six",
                      "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve",
                      "Thirteen", "Fourteen", "Fifteen", "Sixteen",
                      "Seventeen", "Eighteen", "Nineteen"]
        self.tenth = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty",
                      "Seventy", "Eighty", "Ninety"]

    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num < 1000000000:
            return self.under_billion(num)
        elif num % 1000000000 == 0:
            return self.under_thousand(num // 1000000000) + " Billion"
        else:
            return self.under_thousand(num // 1000000000) + " Billion " + self.under_billion(num % 1000000000)


    def under_billion(self, num):
        """
        :type num: int
        :rtype: str
        """
        assert num < 1000000000
        if num < 1000000:
            return self.under_million(num)
        elif num % 1000000 == 0:
            return self.under_thousand(num // 1000000) + " Million"
        else:
            return self.under_thousand(num // 1000000) + " Million " + self.under_million(num % 1000000)


    def under_million(self, num):
        """
        :type num: int
        :rtype: str
        """
        assert num < 1000000
        if num < 1000:
            return self.under_thousand(num)
        elif num % 1000 == 0:
            return self.under_thousand(num // 1000) + " Thousand"
        else:
            return self.under_thousand(num // 1000) + " Thousand " + self.under_thousand(num % 1000)


    def under_hundred(self, num):
        """
        :type num: int
        :rtype: str
        """
        assert num < 100
        if num < 20:
            return self.words[num]
        else:
            if num % 10 == 0:
                return self.tenth[num // 10]
            else:
                return self.tenth[num // 10] + " " + self.words[num % 10]


    def under_thousand(self, num):
        """
        :type num: int
        :rtype: str
        """
        assert num < 1000
        if num >= 100:
            if num % 100 == 0:
                return self.words[num // 100] + " Hundred"
            else:
                return self.words[num // 100] + " Hundred " + self.under_hundred(num % 100)
        else:
            return self.under_hundred(num)

if __name__ == '__main__':
    test = Solution()
    print(test.numberToWords(988))
    print(test.numberToWords(998))
    print(test.numberToWords(123123))
    print(test.numberToWords(12345))