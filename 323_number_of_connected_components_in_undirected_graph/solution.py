from typing import List

class DisjointSet(object):

    def __init__(self, capacity):
        self.forest = list(range(capacity)) # type: List[int]

    def find(self, x: int) -> int:
        if self.forest[x] != x:
            self.forest[x] = self.find(self.forest[x])
        return self.forest[x]

    def union(self, x, y):
        set_x, set_y = self.find(x), self.find(y)
        if set_x == set_y:
            return False
        else:
            self.forest[set_x] = set_y
            return True


class Solution:
    def countComponents(self, n: int, edges : List[List[int]]) -> int:
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        ds = DisjointSet(n)
        for x, y in edges:
            ds.union(x, y)
        return len(set(map(ds.find, range(n))))


if __name__ == '__main__':
    # tests on union find
    test = Solution()
    print(test.countComponents(5, [[0, 1], [1, 2], [3, 4]]))
    print(test.countComponents(5, [[0, 1], [1, 2], [2, 3], [3, 4]]))
    print(test.countComponents(5, [[0, 1], [0, 2], [2, 3], [2, 4]]))

    ds = DisjointSet(10)
    print(ds.find(1))
    print(ds.find(2))
    print(ds.find(3))
    print(ds.union(1, 2))
    print(ds.find(1))
    print(ds.find(2))
    print(ds.find(3))
    print(ds.union(2, 3))
    print(ds.find(1))
    print(ds.find(2))
    print(ds.find(3))
