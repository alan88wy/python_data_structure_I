import tkinter as tk
import time
import threading


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def to_list(self):
        result = []
        curr = self.head
        while curr:
            result.append(curr.data)
            curr = curr.next
        return result


class Visualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Slow–Fast Pointer Visualization (Find Middle Node)")
        self.root.geometry("950x450")
        self.root.config(bg="#eef3ff")

        self.canvas = tk.Canvas(root, width=900, height=300, bg="white")
        self.canvas.pack(pady=20)

        self.status = tk.Label(root, text="", font=("Helvetica", 14), bg="#eef3ff")
        self.status.pack(pady=10)

        self.btn_frame = tk.Frame(root, bg="#eef3ff")
        self.btn_frame.pack(pady=10)

        self.entry = tk.Entry(self.btn_frame, font=("Helvetica", 13), width=40)
        self.entry.grid(row=0, column=0, padx=10)

        self.start_btn = tk.Button(
            self.btn_frame,
            text="Visualize",
            command=self.start_visualization,
            font=("Helvetica", 13, "bold"),
            bg="#3366ff",
            fg="white",
            relief="raised",
        )
        self.start_btn.grid(row=0, column=1, padx=10)

    def start_visualization(self):
        text = self.entry.get().strip()
        if not text:
            self.status.config(text="⚠️ Please enter a list of numbers separated by spaces.")
            return

        # Create linked list
        ll = LinkedList()
        try:
            for num in map(int, text.split()):
                ll.append(num)
        except ValueError:
            self.status.config(text="⚠️ Please enter valid integers.")
            return

        nodes = ll.to_list()
        self.status.config(text="🔄 Finding the middle node...")
        self.canvas.delete("all")

        threading.Thread(target=self.visualize_slow_fast, args=(nodes, ll.head)).start()

    def visualize_slow_fast(self, nodes, head):
        x_start = 80
        y = 150
        box_w = 70
        gap = 40

        # Draw all nodes
        positions = {}
        curr = head
        idx = 0
        while curr:
            x = x_start + idx * (box_w + gap)
            positions[curr] = x
            self.canvas.create_rectangle(x, y - 30, x + box_w, y + 30, fill="#e6e6e6", tags=f"node{idx}")
            self.canvas.create_text(x + box_w / 2, y, text=str(curr.data), font=("Helvetica", 14))
            if curr.next:
                self.canvas.create_line(x + box_w, y, x + box_w + gap, y, arrow=tk.LAST, width=2)
            curr = curr.next
            idx += 1

        self.root.update()

        # Initialize slow and fast pointers
        slow = head
        fast = head
        step = 1

        def highlight_pointer(node, color, label):
            """Draw pointer under node"""
            x = positions[node] + box_w / 2
            pointer_y = y + 45
            self.canvas.create_text(x, pointer_y, text=label, fill=color, font=("Helvetica", 14, "bold"), tags=f"{label}")

        # Animate pointer movement
        while fast and fast.next:
            # Clear old pointers
            self.canvas.delete("slow")
            self.canvas.delete("fast")

            # Highlight current positions
            highlight_pointer(slow, "#33cc33", "slow")
            highlight_pointer(fast, "#ff3333", "fast")

            self.status.config(text=f"Step {step}: slow at {slow.data}, fast at {fast.data}")
            self.root.update()
            time.sleep(1.5)

            slow = slow.next
            fast = fast.next.next
            step += 1

        # Final highlight: middle node
        self.canvas.delete("slow")
        self.canvas.delete("fast")
        if slow:
            highlight_pointer(slow, "#3366ff", "middle")
            self.canvas.itemconfig(f"node{nodes.index(slow.data)}", fill="#99ccff")
            self.status.config(text=f"✅ Middle node found: {slow.data}")

        self.root.update()


# --- Run the App ---
if __name__ == "__main__":
    root = tk.Tk()
    app = Visualizer(root)
    root.mainloop()
