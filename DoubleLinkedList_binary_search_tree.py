class Node:
    """A node in the Binary Search Tree"""
    def __init__(self, data):
        self.data = data
        self.left = None   # points to left child
        self.right = None  # points to right child


class BinarySearchTree:
    """Binary Search Tree using linked nodes"""
    def __init__(self):
        self.root = None

    def insert(self, data):
        """Insert data into the BST"""
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, current, data):
        if data < current.data:
            if current.left is None:
                current.left = Node(data)
            else:
                self._insert_recursive(current.left, data)
        elif data > current.data:
            if current.right is None:
                current.right = Node(data)
            else:
                self._insert_recursive(current.right, data)
        # If data == current.data, ignore (no duplicates)

    def search(self, data):
        """Search for a value in the BST"""
        return self._search_recursive(self.root, data)

    def _search_recursive(self, current, data):
        if current is None:
            return False
        if data == current.data:
            return True
        elif data < current.data:
            return self._search_recursive(current.left, data)
        else:
            return self._search_recursive(current.right, data)

    def inorder(self):
        """Return inorder traversal (sorted order)"""
        print("Root -> ", self.root.data)
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, current, result):
        
        if current:
            self._inorder_recursive(current.left, result)
            result.append(current.data)
            self._inorder_recursive(current.right, result)

    def preorder(self):
        """Return preorder traversal"""
        print("Root -> ", self.root.data)
        result = []
        self._preorder_recursive(self.root, result)
        return result

    def _preorder_recursive(self, current, result):
        if current:
            result.append(current.data)
            self._preorder_recursive(current.left, result)
            self._preorder_recursive(current.right, result)

    def postorder(self):
        """Return postorder traversal"""
        print("Root -> ", self.root.data)
        result = []
        self._postorder_recursive(self.root, result)
        return result

    def _postorder_recursive(self, current, result):
        if current:
            self._postorder_recursive(current.left, result)
            self._postorder_recursive(current.right, result)
            result.append(current.data)

    def minValueNode(self, node):
        """Get the node with the minimum value in the subtree rooted at 'node'"""
        current = node
        
        while current.left is not None:
            current = current.left
            
        return current
    
    """
    How it works:

    1. If the node is a leaf node, remove it by removing the link to it.
    2. If the node only has one child node, connect the parent node of the node you want to remove 
        to that child node.
    3. If the node has both right and left child nodes: Find the node's in-order successor, change values 
        with that node, then delete it.
    
    In step 3 above, the successor we find will always be a leaf node, and because it is the node that 
    comes right after the node we want to delete, we can swap values with it and delete it.
    """
    
    def delete(self, data):
        """Delete a node with a given value"""
        self.root = self._delete_recursive(self.root, data)

    def _delete_recursive(self, current, data):
        if current is None:
            return current

        if data < current.data:
            current.left = self._delete_recursive(current.left, data)
        elif data > current.data:
            current.right = self._delete_recursive(current.right, data)
        else:
            # Node with only one child or no child
            if current.left is None:
                return current.right
            elif current.right is None:
                return current.left

            # Node with two children: Get the inorder successor (smallest in the right subtree)
            min_larger_node = self.minValueNode(current.right)
            current.data = min_larger_node.data
            current.right = self._delete_recursive(current.right, min_larger_node.data)

        return current
    
    

# --- Example Usage ---
if __name__ == "__main__":
    bst = BinarySearchTree()
    data_values = [50, 30, 70, 20, 40, 60, 80]

    for val in data_values:
        bst.insert(val)

    print("Inorder Traversal (sorted):", bst.inorder())
    print("Preorder Traversal:", bst.preorder())
    print("Postorder Traversal:", bst.postorder())

    # Search for values
    print("Search 40:", bst.search(40))
    print("Search 90:", bst.search(90))
    
    # Search for minimum value node
    min_node = bst.minValueNode(bst.root)
    print("Minimum value node:", min_node.data if min_node else "Tree is empty")
    
    
