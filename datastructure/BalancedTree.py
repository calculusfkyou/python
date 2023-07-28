# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isBalanced(self, root):
        if not root:
            return True
        leftHeight=self.isBalanced(root.left)
        if leftHeight==0: 
            return 0
        rightHeight=self.isBalanced(root.right)
        if rightHeight==0: 
            return 0
        if abs(leftHeight-rightHeight)>1: 
            return 0
        return max(leftHeight,rightHeight) + 1