# https://leetcode.com/problems/increasing-order-search-tree/
# Runtime: 160 ms, faster than 59.67% of Python3 online submissions for Increasing Order Search Tree.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def extract_nodes(node):
            if node:
                yield from extract_nodes(node.left)
                yield node.val
                yield from extract_nodes(node.right)

        new_root = node = TreeNode(None)
        for val in extract_nodes(root):
            node.right = TreeNode(val)
            node = node.right
        return new_root.right



s = Solution()
root = TreeNode(5)
root.left = TreeNode(3)
root.left.left = TreeNode(2)
root.left.left.left = TreeNode(1)
root.left.right = TreeNode(4)
root.right = TreeNode(6)
root.right.right = TreeNode(8)
root.right.right.left = TreeNode(7)
root.right.right.right = TreeNode(9)
s.increasingBST(root)
