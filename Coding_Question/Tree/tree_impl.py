
class Node:

    def __init__(self, val, left=None, right=None):
        self.val=val 
        self.left=left
        self.right=right

class Tree:

    def __init__(self):
        self.root=None

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._insert_recursive(self.root, val)

    def _insert_recursive(self, node, val):
        if val<node.val:
            if node.left is None:
                node.left=Node(val)
            else:
                self._insert_recursive(node.left, val)
        else:
            if node.right is None:
                node.right=Node(val)
            else:
                self._insert_recursive(node.right, val)

    def inorder_traversal(self):
        result = []
        self._inorder_traversal(self.root, result)
        return result
    
    def _inorder_traversal(self, node, result):
        if node:
            self._inorder_traversal(node.left, result)
            result.append(node.val)
            self._inorder_traversal(node.right, result)

    def preorder_traversal(self):
        result = []
        self._preorder_traversal(self.root, result)
        return result
    
    def _preorder_traversal(self, node, result):
        if node:
            result.append(node.val)
            self._preorder_traversal(node.left, result)
            self._preorder_traversal(node.right, result)
    
    def postorder_traversal(self):
        result = []
        self._postorder_traversal(self.root, result)
        return result
    
    def _postorder_traversal(self, node, result):
        if node:
            self._postorder_traversal(node.left, result)
            self._postorder_traversal(node.right, result)
            result.append(node.val)

# Example usage
if __name__ == "__main__":
    tree = Tree()
    # Insert nodes
    nodes = [50, 30, 70, 20, 40, 60, 80]
    for node in nodes:
        tree.insert(node)

    # Traversals
    print("Inorder traversal:", tree.inorder_traversal())  # [20, 30, 40, 50, 60, 70, 80]
    print("Preorder traversal:", tree.preorder_traversal())  # [50, 30, 20, 40, 70, 60, 80]
    print("Postorder traversal:", tree.postorder_traversal())  # [20, 40, 30, 60, 80, 70, 50]

    # Search
    # search_value = 40
    # result = tree.search(search_value)
    # print(f"Search for {search_value}: {'Found' if result else 'Not found'}")

