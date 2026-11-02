# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        flag=True
        def height(root):
            nonlocal flag
            if not root:
                return -1
            left_height=height(root.left)
            right_height=height(root.right)

            if abs(left_height-right_height)>1:
                flag=False
            return max(left_height,right_height)+1
        
        h=height(root)
        return flag

        