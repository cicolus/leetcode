from heapq import heappush, heappop
from math import inf
from typing import List, Tuple

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next_node=None):
        self.val = x # type: int
        self.next = next_node # type: ListNode

    def __repr__(self):
        if self.next == None:
            return str(self.val)
        else:
            return str(self.val) + " -> " + str(self.next)

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None
        heap = []

        for idx in range(len(lists)):
            node = lists[idx]
            heappush(heap, (inf if node is None else node.val, idx, node))

        # the following doesn't work because there might be ties, so we use an
        # extra idx to keep track of the original order of the elements
        # for node in lists: # type: ListNode
        #     heappush(heap, (inf if node is None else node.val, node))

        # this doesn't work because might exceed python max recursion depth
        # return self.merge_k_lists(heap)

        condition = True
        dummy_head = ListNode(0)
        prev_node = dummy_head
        while condition:
            min_val, idx, min_node = heappop(heap)  # type: int, ListNode
            if min_val == inf:
                condition = False
            else:
                heappush(heap, (inf if min_node.next is None else min_node.next.val, idx, min_node.next))
                prev_node.next = min_node
                prev_node = min_node

        return dummy_head.next


    # max recursion depth exceeded in this implementation
    def merge_k_lists(self, heap : List[Tuple[int, ListNode]]):
        min_val, idx, min_node = heappop(heap) # type: int, ListNode
        if min_val == inf:
            return None
        else:
            heappush(heap, (inf if min_node.next is None else min_node.next.val, idx, min_node.next))
            min_node.next = self.merge_k_lists(heap)
            return min_node


if __name__ == '__main__':
    list_1 = ListNode(1, ListNode(3, ListNode(5, ListNode(7))))
    list_2 = ListNode(2, ListNode(4, ListNode(6, ListNode(8))))
    print(list_1)
    print(list_2)
    test = Solution()
    print(test.mergeKLists([list_1, list_2]))
    print(test.mergeKLists([]))
    list_1 = ListNode(1, ListNode(1, ListNode(2)))
    list_2 = ListNode(1, ListNode(2, ListNode(2)))
    print(list_1)
    print(list_2)
    print(test.mergeKLists([list_1, list_2]))
