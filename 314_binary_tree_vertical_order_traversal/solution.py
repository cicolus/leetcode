from typing import List, Dict
from queue import Queue


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x # type: int
        self.left = left # type: TreeNode
        self.right = right # type: TreeNode

    def __repr__(self):
        if not self.left and not self.right:
            return "TreeNode(" + str(self.val) + ")"
        return "TreeNode(" + str(self.val) + ", " + str(self.left) + ", " + str(self.right) + ")"

class Solution:
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []

        ret_dict = {} # type:  Dict[int, List[int]]

        q = Queue()
        q.put((root, 0))

        while q.qsize() > 0:
            next_node, index = q.get() # type: TreeNode, int
            if index in ret_dict:
                ret_dict[index].append(next_node.val)
            else:
                ret_dict[index] = [next_node.val]
            if next_node.left != None:
                q.put((next_node.left, index - 1))
            if next_node.right != None:
                q.put((next_node.right, index + 1))

        min_index = min(ret_dict.keys())
        max_index = max(ret_dict.keys())
        return [ret_dict[i] for i in range(min_index, max_index + 1)]


if __name__ == '__main__':
    test = Solution()
    tree_1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    tree_2 = TreeNode(3, TreeNode(9, TreeNode(4), TreeNode(0)),
                         TreeNode(8, TreeNode(1), TreeNode(7)))
    tree_3 = TreeNode(3, TreeNode(9, TreeNode(4), TreeNode(0, right=TreeNode(2))),
                         TreeNode(8, TreeNode(1, TreeNode(5)), TreeNode(7)))
    expected_1 = [[9], [3, 15], [20], [7]]
    expected_2 = [[4], [9], [3, 0, 1], [8], [7]]
    expected_3 = [[4], [9, 5], [3, 0, 1], [8, 2], [7]]
    print(test.verticalOrder(tree_1))
    print(test.verticalOrder(tree_2))
    print(test.verticalOrder(tree_3))