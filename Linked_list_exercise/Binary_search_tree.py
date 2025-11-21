class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_rec(self.root, key)

    def _insert_rec(self, root, key):
        if key < root.val:
            if root.left is None:
                root.left = Node(key)
            else:
                self._insert_rec(root.left, key)
        else:
            if root.right is None:
                root.right = Node(key)
            else:
                self._insert_rec(root.right, key)

    def inorder_traversal(self, root):
        return self._inorder_rec(root)

    def _inorder_rec(self, root):
        res = []
        if root:
            res = self._inorder_rec(root.left)
            res.append(root.val)
            res = res + self._inorder_rec(root.right)
        return res
# Example usage:
bst = BinarySearchTree()
bst.insert(50)
bst.insert(30)
bst.insert(20)
bst.insert(40)
bst.insert(70)
bst.insert(60)
bst.insert(80)
print("Inorder traversal of the BST:", bst.inorder_traversal(bst.root))

# Output: Inorder traversal of the BST: [20, 30, 40, 50, 60, 70, 80]