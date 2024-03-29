"""  4
   /   \
  2     7
 / \   / \
1   3 6   9

     |
     
     4
   /   \
  7     2
 / \   / \
9   6 3   1

"""
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def invertTree(self, root):
        if not root:
            return None
        root.left,root.right=root.right,root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root