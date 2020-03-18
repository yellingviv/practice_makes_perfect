# leetcode problem - return a node and all of its children from a binary tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root.val == val:
            return root
        elif root.val > val and root.left:
            return self.searchBST(root.left, val)
        elif root.val < val and root.right:
            return self.searchBST(root.right, val)
        else:
            return None
        
