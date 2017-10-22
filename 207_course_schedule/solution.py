# there are a total of n courses you have to take, labeled from 0 to (n-1)
# course prerequisite: [0, 1] means that to take course 0 you first have to
# take course 1
#
# Given the total number of courses and a list of prerequisite pairs, is it
# possible for you to finish all courses?

import heapq

example_test_1 = [2, [[0, 1]]]           # possible
example_test_2 = [2, [[0, 1], [1, 0]]]  # impossible

#
#     1
#   /   \
#  0      3 -- 4
#   \   /
#     2
test_1 = [[1, 0], [2, 0], [3, 1], [3, 2], [4, 3]] # possible


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        # Represent the courses as a graph and do Topological sort
        in_degrees = dict(zip([0]*numCourses, range(numCourses)))
        graph = {}

        # build graph

        for prereq in prerequisites:
            need = prereq[1]
            to_take = prereq[0]
            in_degrees[to_take] += 1

            if need not in graph:
                graph[need] = [to_take]
            else:
                graph[need].append(to_take)

        # prepare for Topological sort

        h = []

        for node in in_degrees:
            heapq.heappush(h, (in_degrees[node], node))

        topo_sorted = {}

        # while h:


        pass


if __name__ == '__main__':
    sol = Solution()
    sol.canFinish(4, test_1)