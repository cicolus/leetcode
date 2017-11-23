class Solution:
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """

        initial = A
        counter = 1
        while len(initial) < len(B)+2*len(A):
            if initial.find(B) < 0:
                counter += 1
                initial += A
            else:
                return counter
        return -1

    def repeatedStringMatch_2(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """

        b_chars_set = set()
        for c in B:
            b_chars_set.add(c)

        for c in A:
            if b_chars_set:
                if c in b_chars_set:
                    b_chars_set.remove(c)
                else:
                    break

        if b_chars_set:
            return -1

        counter = 1
        ptr_a, ptr_b = 0, 0
        while ptr_b < len(B):
            if A[ptr_a] == B[ptr_b]:
                ptr_b += 1
            ptr_a += 1
            if ptr_a == len(A):
                ptr_a = 0
                counter += 1

        return counter

    def repeatedStringMatch_revision_1(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """

        b_chars_set = set()
        for c in B:
            b_chars_set.add(c)

        for c in A:
            if b_chars_set:
                if c in b_chars_set:
                    b_chars_set.remove(c)
                else:
                    break

        if b_chars_set:
            return -1

        counter = 1
        ptr_a, ptr_b = 0, 0
        while ptr_b < len(B):
            if A[ptr_a] == B[ptr_b]:
                ptr_a += 1
                ptr_b += 1
                if ptr_a == len(A):
                    ptr_a = 0
                    counter += 1
            else:
                ptr_a += 1

        return counter


if __name__ == '__main__':
    test = Solution()
    print(test.repeatedStringMatch("abcd", "cdabcdab"))
    print(test.repeatedStringMatch("a", "aa"))
    print("a".find("aaa"))