# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        res=[]
        def rec(root,parent,grandparent):
            if root==None:
                return 0
            
            if grandparent and grandparent.val%2==0:
                res.append(root.val)
            rec(root.left,root,parent)
            rec(root.right,root,parent)
        rec(root,None,None)
        return sum(res)
