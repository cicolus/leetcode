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

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root == None:
            return ""
        encoding = []
        def traverse(root : TreeNode):
            if root == None:
                encoding.append(None)
            else:
                encoding.append(root.val)
                traverse(root.left)
                traverse(root.right)

        traverse(root)
        return " ".join(map(str, encoding))


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == '':
            return None
        nodes = list(map(lambda x : None if x == 'None' else int(x), data.split(" ")))
        idx = 0
        def traverse():
            nonlocal idx
            if nodes[idx] == None:
                return None
            else:
                root = TreeNode(nodes[idx])
                idx += 1
                root.left = traverse()
                idx += 1
                root.right = traverse()
                return root

        return traverse()




# Your Codec object will be instantiated and called as such:
if __name__ == '__main__':
    codec = Codec()
    tree = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
    encoding = codec.serialize(tree)
    print(encoding)
    print(codec.deserialize(encoding))
# codec = Codec()
# codec.deserialize(codec.serialize(root))