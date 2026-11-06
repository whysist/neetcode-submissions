# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(node,subNode):
            if node is None and subNode is None:
                return True
            if node is None or subNode is None:
                return False
            if node.val!=subNode.val:
                return False
            return sameTree(node.left,subNode.left) and sameTree(node.right,subNode.right)

        if root is None:
            return subRoot is None
    
        if root.val==subRoot.val and sameTree(root,subRoot):
            return True
        
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
        
        
            

        