import tkinter as tk
from tkinter import messagebox


# --- BST Node ---
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


# --- Binary Search Tree Class ---
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        """Insert a new key into the BST"""
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, root, key):
        if key < root.key:
            if root.left is None:
                root.left = Node(key)
            else:
                self._insert_recursive(root.left, key)
        elif key > root.key:
            if root.right is None:
                root.right = Node(key)
            else:
                self._insert_recursive(root.right, key)

    def search(self, key):
        """Search for a key in the BST"""
        return self._search_recursive(self.root, key)

    def _search_recursive(self, root, key):
        if root is None:
            return False
        if key == root.key:
            return True
        elif key < root.key:
            return self._search_recursive(root.left, key)
        else:
            return self._search_recursive(root.right, key)

    def inorder(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, root, result):
        if root:
            self._inorder_recursive(root.left, result)
            result.append(root.key)
            self._inorder_recursive(root.right, result)


# --- GUI Application ---
class BSTVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Binary Search Tree Visualizer (Linked List Nodes)")
        self.root.geometry("1000x600")
        self.root.configure(bg="#f5f7ff")

        # Initialize BST
        self.bst = BinarySearchTree()

        # --- GUI Layout ---
        tk.Label(root, text="Enter a number:", font=("Helvetica", 13), bg="#f5f7ff").pack(pady=10)
        self.entry = tk.Entry(root, font=("Helvetica", 13))
        self.entry.pack()

        btn_frame = tk.Frame(root, bg="#f5f7ff")
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Insert", font=("Helvetica", 12, "bold"),
                  bg="#4CAF50", fg="white", command=self.insert_node).grid(row=0, column=0, padx=10)
        tk.Button(btn_frame, text="Search", font=("Helvetica", 12, "bold"),
                  bg="#2196F3", fg="white", command=self.search_node).grid(row=0, column=1, padx=10)
        tk.Button(btn_frame, text="Inorder Traversal", font=("Helvetica", 12, "bold"),
                  bg="#9C27B0", fg="white", command=self.show_inorder).grid(row=0, column=2, padx=10)
        tk.Button(btn_frame, text="Clear Tree", font=("Helvetica", 12, "bold"),
                  bg="#f44336", fg="white", command=self.clear_tree).grid(row=0, column=3, padx=10)

        self.canvas = tk.Canvas(root, width=950, height=450, bg="white")
        self.canvas.pack(pady=15)

    # --- Core GUI Logic ---
    def insert_node(self):
        val = self.entry.get().strip()
        if not val.isdigit():
            messagebox.showwarning("Invalid Input", "Please enter a valid integer.")
            return
        val = int(val)
        self.bst.insert(val)
        self.entry.delete(0, tk.END)
        self.redraw_tree()

    def search_node(self):
        val = self.entry.get().strip()
        if not val.isdigit():
            messagebox.showwarning("Invalid Input", "Please enter a valid integer.")
            return
        val = int(val)
        found = self.bst.search(val)
        msg = f"✅ Node {val} found in BST." if found else f"❌ Node {val} not found in BST."
        messagebox.showinfo("Search Result", msg)
        self.entry.delete(0, tk.END)

    def show_inorder(self):
        traversal = self.bst.inorder()
        if traversal:
            messagebox.showinfo("Inorder Traversal", f"Nodes in sorted order:\n{traversal}")
        else:
            messagebox.showinfo("Empty Tree", "No nodes in the tree yet!")

    def clear_tree(self):
        self.bst.root = None
        self.canvas.delete("all")

    def redraw_tree(self):
        self.canvas.delete("all")
        if self.bst.root:
            self._draw_node(self.bst.root, 475, 50, 200)

    def _draw_node(self, node, x, y, dx):
        """Recursively draw each node"""
        if node.left:
            self.canvas.create_line(x, y + 25, x - dx, y + 100 - 25, width=2)
            self._draw_node(node.left, x - dx, y + 100, dx / 2)

        if node.right:
            self.canvas.create_line(x, y + 25, x + dx, y + 100 - 25, width=2)
            self._draw_node(node.right, x + dx, y + 100, dx / 2)

        # Draw current node (circle)
        radius = 25
        self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill="#4CAF50")
        self.canvas.create_text(x, y, text=str(node.key), fill="white", font=("Helvetica", 14, "bold"))


# --- Run App ---
if __name__ == "__main__":
    root = tk.Tk()
    app = BSTVisualizer(root)
    root.mainloop()
