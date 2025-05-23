"""
    Using stack for depth first search
"""
from collections import deque
class TreeNode:

    def __init__(self, val, left=None, right=None):
        self.val=val 
        self.left=left
        self.right=right
        
class BFS:
    
    def __init__(self):
        self._queue=deque()
        
    def BFS_traversal(self, node):
        if not node:
            return 
        self._queue.append(node)
        
        while self._queue:
            node=self._queue.popleft()
            print(node.val, end=" ")
            
            if node.left:
                self._queue.append(node.left)
            if node.right:
                self._queue.append(node.right)
                
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

bfs = BFS()
bfs.BFS_traversal(root)
        