# there are a total of n courses you have to take, labeled from 0 to (n-1)
# course prerequisite: [0, 1] means that to take course 0 you first have to
# take course 1
#
# Given the total number of courses and a list of prerequisite pairs, return
# an ordering of the course to take

import queue

example_test_1 = [2, [[0, 1]]]           # possible
example_test_2 = [2, [[0, 1], [1, 0]]]  # impossible

#
#     1
#   /   \
#  0      3 -- 4
#   \   /
#     2
test_1 = [[1, 0], [2, 0], [3, 1], [3, 2], [4, 3]] # possible

#
#     1    <-
#   /   \     \
#  0      3 -- 4
#   \   /
#     2
test_2 = [[1, 0], [2, 0], [3, 1], [3, 2], [4, 3], [1, 4]] # impossible


class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        # Represent the courses as a graph and do Topological sort
        in_degrees = dict(zip(list(range(numCourses)), [0]*numCourses))
        graph = dict(zip(list(range(numCourses)), [[] for i in range(numCourses)]))

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

        q = queue.Queue()

        for node in in_degrees:
            if in_degrees[node] == 0:
                q.put(node)

        topo_sorted = []

        # topological sort

        while q.qsize() > 0:
            node = q.get()
            topo_sorted.append(node)
            for adj in graph[node]:
                in_degrees[adj] -= 1
                if in_degrees[adj] == 0:
                    q.put(adj)

        if len(topo_sorted) == numCourses:
            return topo_sorted
        else:
            return []


if __name__ == '__main__':
    sol = Solution()
    print(sol.findOrder(5, test_1))
    print(sol.findOrder(5, test_2))