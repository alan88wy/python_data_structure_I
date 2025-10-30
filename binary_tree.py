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
          
# Example Usage:
if __name__ == "__main__":
    # Create the binary tree and insert nodes
    bt = BinaryTree(TreeNode(10))
    bt.insert(5)
    bt.insert(15)
    bt.insert(3)
    bt.insert(7)
    bt.insert(12)
    bt.insert(18)

    # The binary tree now has the following structure:
    #         10
    #        /  \
    #       5    15
    #      / \   / \
    #     3   7 12 18

    print("Binary Tree Root:", bt.root.data)  # Output: 10
    print("Left Child of Root:", bt.root.left.data)  # Output: 5
    print("Right Child of Root:", bt.root.right.data)  # Output: 15