# https://leetcode.com/problems/trim-a-binary-search-tree/
# Runtime: 64 ms, faster than 68.75% of Python3 online submissions for Trim a Binary Search Tree.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        def trim(node):
            if node is None:
                return None
            elif node.val < L:
                return trim(node.right)
            elif node.val > R:
                return trim(node.left)
            else:
                node.left = trim(node.left)
                node.right = trim(node.right)
                return node



s = Solution()
root = TreeNode(3)
root.right = TreeNode(4)
root.left = TreeNode(0)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(1)
print(s.trimBST(root, 1, 3))