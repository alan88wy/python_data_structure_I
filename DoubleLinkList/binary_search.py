"""
How it works:
*************

1. Check the value in the center of the array.
2. If the target value is lower, search the left half of the array. If the target value is higher, 
   search the right half.
3. Continue step 1 and 2 for the new reduced part of the array until the target value is found or 
   until the search area is empty.
4. If the value is found, return the target value index. If the target value is not found, return -1.
"""

class Node:
    """Node of a doubly linked list"""
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    """Sorted doubly linked list"""
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        """Insert in sorted order"""
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
            return

        # Insert at the correct sorted position
        current = self.head
        while current and current.data < data:
            current = current.next

        if current is None:
            # Insert at end
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        elif current == self.head:
            # Insert at beginning
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        else:
            # Insert in the middle
            prev_node = current.prev
            prev_node.next = new_node
            new_node.prev = prev_node
            new_node.next = current
            current.prev = new_node

    def display(self):
        """Display the list elements"""
        values = []
        current = self.head
        while current:
            values.append(current.data)
            current = current.next
        return values
    
    """
    Binary Search Logic

    We maintain two pointers:
    left (start node) and right (end node).

    Find the middle node between them using a “slow–fast” pointer approach.

    Compare mid.data to the target:

    1. If equal → found 🎯
    2. If smaller → move left to mid.next
    3. If larger → move right to mid.prev

    Continue until left passes right.
    """
    
    def binary_search(self, target):
        """Binary search on doubly linked list"""
        left = self.head
        right = self.tail

        while left and right and left != right.next:
            mid = self._get_middle(left, right)

            if mid is None:
                return False

            if mid.data == target:
                return True
            elif mid.data < target:
                left = mid.next
            else:
                right = mid.prev

        return False

    def _get_middle(self, left, right):
        """Helper to find the middle node between left and right (inclusive)"""
        if left is None or right is None:
            return None

        slow = left
        fast = left

        while fast != right and fast.next != right:
            fast = fast.next.next if fast.next else None
            slow = slow.next

        return slow


# --- Example Usage ---
if __name__ == "__main__":
    dll = DoublyLinkedList()

    for val in [10, 20, 30, 40, 50, 60, 70]:
        dll.append(val)

    print("Sorted Doubly Linked List:", dll.display())

    targets = [30, 45, 70, 5]
    for t in targets:
        found = dll.binary_search(t)
        print(f"Search {t}: {'✅ Found' if found else '❌ Not Found'}")
