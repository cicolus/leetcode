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
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if root is None:
            return root
        if root.val == key:
            if not root.left and not root.right:
                return None
            if root.left:
                if not root.left.right:
                    root.left.right = root.right
                    return root.left
                else:
                    curr = root.left
                    while curr.right.right != None:
                        curr = curr.right
                    root.val = curr.right.val
                    curr.right = curr.right.left
            else:
                if not root.right.left:
                    root.right.left = root.left
                    return root.right
                else:
                    curr = root.right
                    while curr.left.left != None:
                        curr = curr.left
                    root.val = curr.left.val
                    curr.left = curr.left.right
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        return root



if __name__ == '__main__':
    sample_tree = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(6, None, TreeNode(7)))
    test = Solution()
    print(sample_tree)
    result = test.deleteNode(sample_tree, 3)
    print(result)
    sample_tree = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(6, None, TreeNode(7)))
    result = test.deleteNode(sample_tree, 2)
    print(result)
    sample_tree = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(6, None, TreeNode(7)))
    result = test.deleteNode(sample_tree, 4)
    print(result)
    sample_tree = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(6, None, TreeNode(7)))
    result = test.deleteNode(sample_tree, 5)
    print(result)
    sample_tree = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(6, None, TreeNode(7)))
    result = test.deleteNode(sample_tree, 6)
    print(result)
    sample_tree = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(6, None, TreeNode(7)))
    result = test.deleteNode(sample_tree, 7)
    print(result)
