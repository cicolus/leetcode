from typing import Tuple

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left # type: TreeNode
        self.right = right # type: TreeNode

class Solution:
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        else:
            return max(self.helper(root)) - 1

    def helper(self, root):
        """
        :type root: TreeNode
        :rtype: Tuple[int, int]
        """
        if root.left == None and root.right == None:
            return (1, 1)
        elif root.left != None and root.right != None:
            left_max, left_extensible = self.helper(root.left)
            right_max, right_extensible = self.helper(root.right)
            curr_extensible = 1
            if root.val == root.left.val:
                curr_extensible = left_extensible + 1
            if root.val == root.right.val:
                curr_extensible = max(curr_extensible, right_extensible + 1)
            curr_max = max(left_max, right_max, curr_extensible)
            if root.val == root.left.val and root.val == root.right.val:
                curr_max = max(curr_max, 1 + left_extensible + right_extensible)
            return (curr_max, curr_extensible)
        elif root.left != None:
            left_max, left_extensible = self.helper(root.left)
            curr_extensible = 1
            if root.val == root.left.val:
                curr_extensible = left_extensible + 1
            curr_max = max(left_max, curr_extensible)
            if root.val == root.left.val:
                curr_max = max(curr_max, 1 + left_extensible)
            return (curr_max, curr_extensible)
        else:
            right_max, right_extensible = self.helper(root.right)
            curr_extensible = 1
            if root.val == root.right.val:
                curr_extensible = right_extensible + 1
            curr_max = max(right_max, curr_extensible)
            if root.val == root.right.val:
                curr_max = max(curr_max, 1 + right_extensible)
            return (curr_max, curr_extensible)

if __name__ == '__main__':
    tree = TreeNode(5, TreeNode(4, TreeNode(1), TreeNode(1)), TreeNode(5, right=TreeNode(5)))
    test = Solution()
    print(test.longestUnivaluePath(tree))