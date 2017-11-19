class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """

        def is_self_dividing(num):
            x = filter(lambda x: True if x == '0' else num % int(x) != 0, list(str(num)))
            return len(list(x)) == 0

        return list(filter(is_self_dividing, range(left, right + 1)))

if __name__ == '__main__':
    test = Solution()
    print(test.selfDividingNumbers(1, 22))