from typing import Tuple

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        """
        :type x: int
        :type left: TreeNode
        :type right: TreeNode
        """
        self.val = x # type: int
        self.left = left # type: TreeNode
        self.right = right # type: TreeNode

class Solution:
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return max(self.helper(root))

    def helper(self, root):
        """
        :type root: TreeNode
        :rtype: Tuple[int, int, int]
        """
        if root == None:
            return (0, 0)
        elif root.left is None and root.right is None:
            return(root.val, root.val)
        elif root.left != None and root.right != None:
            left_max, left_extensible = self.helper(root.left)
            right_max, right_extensible = self.helper(root.right)
            ret_max = max([left_max, right_max, left_extensible, right_extensible,
                           root.val + left_extensible, root.val, root.val + right_extensible,
                           root.val + left_extensible + right_extensible])
            ret_extensible = max([root.val + left_extensible, root.val, root.val + right_extensible])
            return (ret_max, ret_extensible)
        elif root.left != None:
            left_max, left_extensible = self.helper(root.left)
            ret_max = max([left_max, left_extensible, root.val + left_extensible, root.val])
            ret_extensible = max([root.val + left_extensible, root.val])
            return (ret_max, ret_extensible)
        else:
            right_max, right_extensible = self.helper(root.right)
            ret_max = max([right_max, right_extensible, root.val, root.val + right_extensible])
            ret_extensible = max([root.val, root.val + right_extensible])
            return (ret_max, ret_extensible)


if __name__ == '__main__':
    test = Solution()
    tree_1 = TreeNode(1, TreeNode(2), TreeNode(3))
    tree_2 = TreeNode(9, TreeNode(-10, TreeNode(99, TreeNode(98, TreeNode(-10), TreeNode(99, TreeNode(99)))),
                                       TreeNode(-5, TreeNode(-6))),
                         TreeNode(-20, right=TreeNode(10, right=TreeNode(10))))
    tree_3 = TreeNode(-3)
    print(test.maxPathSum(tree_1))
    print(test.maxPathSum(tree_2))
    print(test.maxPathSum(tree_3))