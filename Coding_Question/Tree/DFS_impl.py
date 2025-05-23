"""
    Using stack for depth first search
"""
class TreeNode:

    def __init__(self, val, left=None, right=None):
        self.val=val 
        self.left=left
        self.right=right
        
class DFS:
    
    def __init__(self):
        self._stack=[]
        
    def DFS_traversal(self, node):
        if not node:
            return 
        self._stack.append(node)
        
        while self._stack:
            node=self._stack.pop()
            print(node.val, end=" ")
            
            if node.right:
                self._stack.append(node.right)
            if node.left:
                self._stack.append(node.left)
                
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

dfs = DFS()
dfs.DFS_traversal(root)
        