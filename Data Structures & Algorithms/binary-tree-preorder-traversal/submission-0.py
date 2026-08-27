# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pre(self,root:Optional[TreeNode],res:List[int]):
        if root:
            res.append(root.val)
            self.pre(root.left,res)
            self.pre(root.right,res)
        

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        self.pre(root,res)
        return res
        