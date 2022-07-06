from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        
        def bfs(root):
            
            q=deque()
            q.append(root)
            res=[]
            while q:
                level=[]
                for i in range(len(q)):
                    node=q.popleft()
                    level.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                if level:
                    res.append(level)
            return sum(res[-1])
        return bfs(root)
