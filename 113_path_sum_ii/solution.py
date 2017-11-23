from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left # type: TreeNode
        self.right = right # type: TreeNode

class Solution:
    def pathSum(self, root, target_sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        solution = []
        def helper(h_root, curr_sum, stack_trace : List[int]):
            """
            :type root: TreeNode
            :type curr_sum: int
            :type stack_trace: List[int]
            """
            if h_root is None:
                return
            if h_root.left == None and h_root.right == None:
                if curr_sum + h_root.val == target_sum:
                    stack_trace.append(h_root.val)
                    solution.append(stack_trace)
            elif h_root.left != None and h_root.right != None:
                left_copy = stack_trace.copy()
                left_copy.append(h_root.val)
                right_copy = stack_trace.copy()
                right_copy.append(h_root.val)
                helper(h_root.left, curr_sum + h_root.val, left_copy)
                helper(h_root.right, curr_sum + h_root.val, right_copy)
            elif h_root.left != None:
                left_copy = stack_trace.copy()
                left_copy.append(h_root.val)
                helper(h_root.left, curr_sum + h_root.val, left_copy)
            else:
                right_copy = stack_trace.copy()
                right_copy.append(h_root.val)
                helper(h_root.right, curr_sum + h_root.val, right_copy)
        helper(root, 0, [])
        return solution



if __name__ == '__main__':
    tree_1 = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))),
                    TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(5), TreeNode(1))))
    tree_2 = None
    test = Solution()
    print(test.pathSum(tree_1, 22))
    print(test.pathSum(tree_2, 0))
