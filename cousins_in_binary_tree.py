from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        
        def bfs(root,x,y):
            q=deque()
            q.append((0,root,None))
            xpar,ypar=None,None
            xh,yh=0,0
            while q:
                height,node,parent=q.popleft()
                
                if node.val==x:
                    xpar=parent
                    xh=height
                if node.val==y:
                    ypar=parent
                    yh=height
                if node.left:    
                    q.append((height+1,node.left,node))
                if node.right:
                    q.append((height+1,node.right,node))
                
            return xh==yh and xpar!=ypar
        return bfs(root,x,y)
