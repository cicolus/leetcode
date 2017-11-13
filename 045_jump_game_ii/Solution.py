from queue import PriorityQueue
from typing import List


class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 1:
            return 0
        curr_step_max = 0
        next_step_max = 0
        curr_steps = 0
        for i in range(length):
            if i > curr_step_max:
                curr_steps += 1
                curr_step_max = next_step_max
            next_step_max = max(next_step_max, i + nums[i])
            if next_step_max >= (length - 1):
                return curr_steps + 1

    def jump_bfs(self, nums):
        """
        TLE, don't use
        :type nums: List[int]
        :rtype: int
        """
        graph = {}
        for index in range(len(nums)):
            graph[index] = []

        for index, length in zip(range(len(nums)), nums):
            graph[index] += list(map(lambda x : index + x, range(1, length + 1)))

        # BFS, A*
        q = PriorityQueue()
        dest = len(nums) - 1
        visited = set()

        q.put((dest, 0, 0))

        visited.add(0)
        while q.qsize() != 0:
            _, jumps, node = q.get()
            node = -node
            if node == dest:
                return jumps
            for next_node in graph[node]:
                if next_node not in visited:
                    visited.add(next_node)
                    heuristic = dest - next_node
                    q.put((-heuristic, jumps + 1, -next_node))
