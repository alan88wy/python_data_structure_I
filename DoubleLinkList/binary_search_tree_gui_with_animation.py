import tkinter as tk
from tkinter import messagebox


# --- Node class (Linked List Node for BST) ---
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


# --- Binary Search Tree Structure ---
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        """Insert a key into the BST"""
        if self.root is None:
            self.root = Node(key)
            return [self.root]  # Return path (for animation)
        return self._insert_recursive(self.root, key, path=[self.root])

    def _insert_recursive(self, node, key, path):
        if key < node.key:
            if node.left:
                path.append(node.left)
                return self._insert_recursive(node.left, key, path)
            else:
                node.left = Node(key)
                path.append(node.left)
                return path
        elif key > node.key:
            if node.right:
                path.append(node.right)
                return self._insert_recursive(node.right, key, path)
            else:
                node.right = Node(key)
                path.append(node.right)
                return path
        return path  # duplicate key ignored

    def search(self, key):
        """Return traversal path while searching for key"""
        node = self.root
        path = []
        while node:
            path.append(node)
            if key == node.key:
                break
            elif key < node.key:
                node = node.left
            else:
                node = node.right
        return path

    def inorder(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.key)
            self._inorder_recursive(node.right, result)


# --- GUI Class with Animation ---
class BSTVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Animated Binary Search Tree Visualizer 🌳")
        self.root.geometry("1100x700")
        self.root.configure(bg="#eef3ff")

        # Data
        self.bst = BinarySearchTree()
        self.node_positions = {}
        self.animation_speed = 600  # milliseconds per step

        # --- GUI Elements ---
        tk.Label(root, text="Enter a number:", font=("Helvetica", 14), bg="#eef3ff").pack(pady=10)
        self.entry = tk.Entry(root, font=("Helvetica", 14))
        self.entry.pack()

        btn_frame = tk.Frame(root, bg="#eef3ff")
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Insert", font=("Helvetica", 12, "bold"),
                  bg="#4CAF50", fg="white", command=self.insert_with_animation).grid(row=0, column=0, padx=10)
        tk.Button(btn_frame, text="Search", font=("Helvetica", 12, "bold"),
                  bg="#2196F3", fg="white", command=self.search_with_animation).grid(row=0, column=1, padx=10)
        tk.Button(btn_frame, text="Inorder Traversal", font=("Helvetica", 12, "bold"),
                  bg="#9C27B0", fg="white", command=self.show_inorder).grid(row=0, column=2, padx=10)
        tk.Button(btn_frame, text="Clear Tree", font=("Helvetica", 12, "bold"),
                  bg="#f44336", fg="white", command=self.clear_tree).grid(row=0, column=3, padx=10)

        self.canvas = tk.Canvas(root, width=1050, height=500, bg="white")
        self.canvas.pack(pady=20)

    # --- Helper: Draw Tree ---
    def draw_tree(self):
        self.canvas.delete("all")
        self.node_positions = {}
        if self.bst.root:
            self._draw_node(self.bst.root, 525, 50, 250)

    def _draw_node(self, node, x, y, dx):
        if node.left:
            self.canvas.create_line(x, y + 25, x - dx, y + 100 - 25, width=2)
            self._draw_node(node.left, x - dx, y + 100, dx / 2)
        if node.right:
            self.canvas.create_line(x, y + 25, x + dx, y + 100 - 25, width=2)
            self._draw_node(node.right, x + dx, y + 100, dx / 2)

        self.node_positions[node] = (x, y)
        self._draw_circle(x, y, str(node.key), fill="#4CAF50")

    def _draw_circle(self, x, y, text, fill="#4CAF50"):
        r = 25
        self.canvas.create_oval(x - r, y - r, x + r, y + r, fill=fill, outline="black")
        self.canvas.create_text(x, y, text=text, font=("Helvetica", 13, "bold"), fill="white")

    # --- Animation Logic ---
    def animate_path(self, path, final_color="#4CAF50", message=None):
        if not path:
            return
        def step(i):
            if i > 0:
                # restore previous node
                x, y = self.node_positions[path[i - 1]]
                self._draw_circle(x, y, str(path[i - 1].key))

            if i < len(path):
                x, y = self.node_positions[path[i]]
                # highlight current node
                self._draw_circle(x, y, str(path[i].key), fill="#FFD700")  # yellow
                self.root.after(self.animation_speed, step, i + 1)
            else:
                # final node coloring
                x, y = self.node_positions[path[-1]]
                self._draw_circle(x, y, str(path[-1].key), fill=final_color)
                if message:
                    messagebox.showinfo("Result", message)

        step(0)

    # --- Insert with Animation ---
    def insert_with_animation(self):
        val = self.entry.get().strip()
        if not val.isdigit():
            messagebox.showwarning("Invalid Input", "Please enter a valid integer.")
            return
        val = int(val)
        path = self.bst.insert(val)
        self.entry.delete(0, tk.END)
        self.draw_tree()
        # Animate path (red for insertion)
        self.root.after(500, lambda: self.animate_path(path, final_color="#FF5733", message=f"✅ Inserted {val}"))

    # --- Search with Animation ---
    def search_with_animation(self):
        val = self.entry.get().strip()
        if not val.isdigit():
            messagebox.showwarning("Invalid Input", "Please enter a valid integer.")
            return
        val = int(val)
        path = self.bst.search(val)
        self.entry.delete(0, tk.END)
        self.draw_tree()
        if not path:
            messagebox.showinfo("Search Result", f"❌ Tree is empty.")
            return
        found = path[-1].key == val
        color = "#4CAF50" if found else "#f44336"
        msg = f"✅ Node {val} found." if found else f"❌ Node {val} not found."
        self.root.after(500, lambda: self.animate_path(path, final_color=color, message=msg))

    # --- Traversal and Clear ---
    def show_inorder(self):
        traversal = self.bst.inorder()
        if traversal:
            messagebox.showinfo("Inorder Traversal", f"Nodes in sorted order:\n{traversal}")
        else:
            messagebox.showinfo("Empty Tree", "No nodes in the tree yet!")

    def clear_tree(self):
        self.bst.root = None
        self.canvas.delete("all")
        self.node_positions.clear()


# --- Run the GUI ---
if __name__ == "__main__":
    root = tk.Tk()
    app = BSTVisualizer(root)
    app.draw_tree()
    root.mainloop()
