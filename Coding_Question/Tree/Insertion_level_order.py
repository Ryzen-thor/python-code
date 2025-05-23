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
    
        
    def BFS_traversal(self, node):
        if not node:
            return 
        queue = deque()
        queue.append(node)
        
        while queue:
            node=queue.popleft()
            print(node.val, end=" ")
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
    def _insert(self, node, val):
        if not node:
            return 
        queue = deque()
        queue.append(node)
        
        while queue:
            node=queue.popleft()
            
            if node.left is None:
                node.left=TreeNode(val)
                break
            elif node.right is None:
                node.right=TreeNode(val)
                break
            else:
                queue.append(node.left)
                queue.append(node.right)
    
    def _delete(self, node):
        temp=node
        node_val=node.val
        while node.right or node.left:
            if node.right:
                node.right.val, node.val = node.val, node.right.val
                temp=node
                node=node.right
            elif node.left:
                node.left.val, node.val = node.val, node.left.val
                temp=node
                node=node.left
        
            if temp.left.val == node_val:
                temp.left=None
            else:
                temp.right=None
            
                
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

bfs = BFS()
bfs.BFS_traversal(root)
print()
bfs._insert(root,7)
bfs.BFS_traversal(root)
print()
bfs._delete(root.right)
bfs.BFS_traversal(root)
        