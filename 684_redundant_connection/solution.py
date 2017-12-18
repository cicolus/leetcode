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
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        ds = DisjointSet(len(edges) + 1)
        for x, y in edges:
            if not ds.union(x, y):
                return [x, y]

if __name__ == '__main__':
    test = Solution()
    print(test.findRedundantConnection([[1,2], [1,3], [2,3]]))
    print(test.findRedundantConnection([[1,2], [2,3], [3,4], [1,4], [1,5]]))