class TreeNode: 
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root):
        self.root = root
        self.size = 0

    def insert(self, data):
        if not self.root:
            self.root = TreeNode(data)
            self.size += 1
            return

        current = self.root
        
        while True:
            if data < current.data:
                if current.left:
                    current = current.left
                else:
                    current.left = TreeNode(data)
                    self.size += 1
                    return
            else:
                if current.right:
                    current = current.right
                else:
                    current.right = TreeNode(data)
                    self.size += 1
                    return

    # -----------------------------------------
    # REVERSE (MIRROR) BINARY TREE FUNCTION
    # -----------------------------------------
    def reverse(self, node=None):
        if node is None:
            node = self.root

        # if node is None:
        #     return None
        
        # swap children
        node.left, node.right = node.right, node.left
        
        # recursively reverse subtrees
        if node.left:
            self.reverse(node.left)
        if node.right:
            self.reverse(node.right)

        return node


# Example Usage:
if __name__ == "__main__":
    bt = BinaryTree(TreeNode(10))
    bt.insert(5)
    bt.insert(15)
    bt.insert(3)
    bt.insert(7)
    bt.insert(12)
    bt.insert(18)

    # before reverse:
    #         10
    #        /  \
    #       5    15
    #      / \   / \
    #     3   7 12 18

    print("Before reverse:")
    print("-----------------------------------")
    print("Root:", bt.root.data)                     # 10
    print("Left Child of Root:", bt.root.left.data)   # 5
    print("Right Child of Root:", bt.root.right.data) # 15
    print("Left Child of Left Child:", bt.root.left.left.data)   # 3
    print("Right Child of Left Child:", bt.root.left.right.data) # 7
    print("Left Child of Right Child:", bt.root.right.left.data)   # 12
    print("Right Child of Right Child:", bt.root.right.right.data) # 18
    
    bt.reverse()   # MIRROR THE TREE

    # after reverse:
    #         10
    #        /  \
    #      15    5
    #     / \   / \
    #   18 12  7   3

    print("\nAfter reverse:")
    print("-----------------------------------")
    print("Root:", bt.root.data)                     # 10
    print("Left Child of Root:", bt.root.left.data)   # 15
    print("Right Child of Root:", bt.root.right.data) # 5
    print("Left Child of Left Child:", bt.root.left.left.data)   # 18
    print("Right Child of Left Child:", bt.root.left.right.data) # 12
    print("Left Child of Right Child:", bt.root.right.left.data)   # 7
    print("Right Child of Right Child:", bt.root.right.right.data) # 3
    