import tkinter as tk
from tkinter import messagebox


# --- Doubly Linked List Node ---
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


# --- Doubly Linked List Class ---
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def clear(self):
        self.head = self.tail = None

    def is_palindrome(self):
        left = self.head
        right = self.tail

        while left and right and left != right and right.next != left:
            if left.data != right.data:
                return False
            left = left.next
            right = right.prev

        return True

    def to_list(self):
        result = []
        curr = self.head
        while curr:
            result.append(curr.data)
            curr = curr.next
        return result


# --- GUI App ---
class PalindromeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Doubly Linked List Palindrome Checker")
        self.root.geometry("800x400")
        self.root.config(bg="#f0f4ff")

        self.dll = DoublyLinkedList()

        self.label = tk.Label(
            root,
            text="Enter a string to check:",
            font=("Helvetica", 14),
            bg="#f0f4ff",
        )
        self.label.pack(pady=10)

        self.entry = tk.Entry(root, font=("Helvetica", 14), width=50)
        self.entry.pack(pady=5)

        self.check_btn = tk.Button(
            root,
            text="Check Palindrome",
            font=("Helvetica", 13, "bold"),
            command=self.check_palindrome,
            bg="#3366ff",
            fg="white",
            relief="raised",
            padx=10,
            pady=5,
        )
        self.check_btn.pack(pady=10)

        self.canvas = tk.Canvas(root, width=760, height=200, bg="white")
        self.canvas.pack(pady=15)

    def draw_linked_list(self, nodes, is_palindrome):
        """Draw the doubly linked list nodes on the canvas"""
        self.canvas.delete("all")

        x_start = 60
        y = 100
        node_width = 60
        gap = 40

        for i, data in enumerate(nodes):
            x = x_start + i * (node_width + gap)
            color = "#66cc66" if is_palindrome else "#ff6666"
            self.canvas.create_rectangle(x, y - 30, x + node_width, y + 30, fill=color)
            self.canvas.create_text(x + node_width / 2, y, text=data, font=("Helvetica", 16, "bold"))

            # Draw arrows
            if i < len(nodes) - 1:
                self.canvas.create_line(
                    x + node_width, y, x + node_width + gap, y, arrow=tk.LAST, width=2
                )
                self.canvas.create_line(
                    x + node_width + gap - 10, y - 5, x + node_width + 10, y - 5, arrow=tk.FIRST, width=2
                )

    def check_palindrome(self):
        text = self.entry.get().strip()
        if not text:
            messagebox.showwarning("Input Required", "Please enter a string.")
            return

        # Build linked list
        self.dll.clear()
        for ch in text:
            if ch.isalnum():
                self.dll.append(ch.lower())

        nodes = self.dll.to_list()
        if not nodes:
            messagebox.showwarning("Invalid Input", "Please enter at least one alphanumeric character.")
            return

        is_pal = self.dll.is_palindrome()
        self.draw_linked_list(nodes, is_pal)

        if is_pal:
            messagebox.showinfo("Result", "✅ It's a palindrome!")
        else:
            messagebox.showinfo("Result", "❌ Not a palindrome.")


# --- Run the app ---
if __name__ == "__main__":
    root = tk.Tk()
    app = PalindromeApp(root)
    root.mainloop()
