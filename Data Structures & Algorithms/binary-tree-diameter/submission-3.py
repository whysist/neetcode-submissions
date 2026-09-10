# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans=float('-inf')
        # ans=float('-inf')
        def height(root):
            nonlocal ans
            if not root:
                return -1
            left_h=height(root.left)
            right_h=height(root.right)
            current_h=max(left_h,right_h)+1

            ans=max(ans,left_h+right_h+2)
            return current_h
        # ans=float('-inf')
        # def diameter(root):
        #     if not root:
        #         return 0
        #     return max(ans,height(root.left)+height(root.right))
        hei=height(root)
        return ans