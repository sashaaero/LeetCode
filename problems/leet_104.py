# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Runtime: 48 ms, faster than 98.26% of Python3 online submissions for Maximum Depth of Binary Tree.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        depths = set()
        def deeper(node, level):
            if node:
                depths.add(level)
                deeper(node.left, level + 1)
                deeper(node.right, level + 1)

        deeper(root, 1)
        return max(depths) if depths else 0