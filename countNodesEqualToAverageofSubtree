# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        
        count=0
        def rec(root):
            nonlocal count
            if root==None:    
                return [0,0]

            if root.left==None and root.right==None:
                count+=1
                return [root.val,1]
            
            l=rec(root.left)
            r=rec(root.right)
            
            sum1=root.val+l[0]+r[0]
            nodes=1+l[1]+r[1]
            
            if root.val==sum1//nodes:
                count+=1
            
            return [sum1,nodes]
            
            
        rec(root)
        #print(count)        
        return count
