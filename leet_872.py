# https://leetcode.com/problems/leaf-similar-trees/
# Runtime: 36 ms, faster than 99.28% of Python3 online submissions for Leaf-Similar Trees.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

root = TreeNode(3)
root.left = TreeNode(5)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)
root.right = TreeNode(1)
root.right.left = TreeNode(9)
root.right.right = TreeNode(8)

root2 = TreeNode(3)
root2.left = TreeNode(5)
root2.left.left = TreeNode(6)
root2.left.right = TreeNode(2)
root2.left.right.left = TreeNode(7)
root2.left.right.right = TreeNode(4)
root2.right = TreeNode(1)
root2.right.left = TreeNode(9)
root2.right.right = TreeNode(8)

def extract_values(node):
    if node.left is None and node.right is None:
        yield node.val
    else:
        if node.left:
            yield from extract_values(node.left)
        if node.right:
            yield from extract_values(node.right)


def check_vales(root1, root2):
    gen1 = extract_values(root1)
    gen2 = extract_values(root2)
    while True:
        try:
            val1 = next(gen1)
            try:
                val2 = next(gen2)
                if val1 != val2:
                    return False
            except StopIteration:
                return False
        except StopIteration:
            try:
                val2 = next(gen2)
                return False
            except StopIteration:
                return True

print(check_vales(root, root2))
