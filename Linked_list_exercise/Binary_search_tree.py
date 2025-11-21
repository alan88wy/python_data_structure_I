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

    # Insert a new node with the given key
    def _insert_rec(self, root, key):
        # Recursive helper function to insert a new node
        if key < root.val:
            # Go to the left subtree
            # If left child is None, insert here
            if root.left is None:
                root.left = Node(key)
            else:
                # Recur on the left subtree
                self._insert_rec(root.left, key)
        # Go to the right subtree
        else:
            if root.right is None:
                root.right = Node(key)
            else:
                # Recur on the right subtree
                self._insert_rec(root.right, key)

    def inorder_traversal(self, root):
        return self._inorder_rec(root)

    # Inorder traversal of the BST
    def _inorder_rec(self, root):
        res = []
        if root:
            res = self._inorder_rec(root.left)
            res.append(root.val)
            res = res + self._inorder_rec(root.right)
        return res
    
    def search(self, key):
        return self._search_rec(self.root, key)
    
    # Search for a node with the given key
    def _search_rec(self, root, key):
        if root is None or root.val == key:
            return root
        
        # Key is smaller than root's key
        if key < root.val:
            # Recur on the left subtree
            return self._search_rec(root.left, key)
        
        # Key is greater than root's key
        return self._search_rec(root.right, key)
    
    # Delete a node with the given key
    def delete(self, key):
        self.root = self._delete_rec(self.root, key)
        
    # Delete a node with the given key and return the new root
    def _delete_rec(self, root, key):
        if root is None:
            return root
        if key < root.val:
            # Recur on the left subtree
            root.left = self._delete_rec(root.left, key)
        elif key > root.val:
            # Recur on the right subtree
            root.right = self._delete_rec(root.right, key)
        else:
            # Node with only one child or no child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            
            # Node with two children: Get the inorder successor 
            # (smallest in the right subtree)
            temp = self._min_value_node(root.right)
            
            # Copy the inorder successor's content to this node
            root.val = temp.val
            
            # Delete the inorder successor
            root.right = self._delete_rec(root.right, temp.val)
            
        return root
    
    # Get the node with the minimum value in the given subtree
    def _min_value_node(self, node):
        current = node
        
        # Loop down to find the leftmost leaf
        while current.left is not None:
            current = current.left
            
        return current
    
# Example usage:
bst = BinarySearchTree()
bst.insert(50)
bst.insert(30)
bst.insert(20)
bst.insert(40)
bst.insert(70)
bst.insert(60)
bst.insert(80)
bst.insert(17)
bst.insert(19)
bst.insert(25)
bst.insert(27)
bst.insert(31)
bst.insert(35)
bst.insert(41)
bst.insert(45)


print("Inorder traversal of the BST:", bst.inorder_traversal(bst.root))
# Output: Inorder traversal of the BST: [17, 19, 20, 25, 27, 30, 31, 35, 40, 41, 45, 50, 60, 70, 80]

# Searching for a value
result = bst.search(41)

if result:
    print("Found:", result.val)
else:
    print("Not Found")

# Deleting a value
bst.delete(20)
print("Inorder traversal after deleting 20:", bst.inorder_traversal(bst.root))

