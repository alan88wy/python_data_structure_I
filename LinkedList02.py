class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    """
    LinkedList - A singly linked list implementation for managing a collection of nodes.
    This class provides a complete implementation of a singly linked list with operations
    to insert, remove, retrieve, and manipulate elements.
    Attributes:
        head (Node): Reference to the first node in the linked list.
        tail (Node): Reference to the last node in the linked list.
        length (int): The total number of nodes currently in the linked list.
    Methods:
        __init__(value):
            Initializes a new LinkedList with a single node containing the given value.
            Sets both head and tail to point to this node, and length to 1.
        add(value):
            Appends a new node with the given value to the end of the linked list.
            Updates the tail pointer and increments length.
            Time Complexity: O(1)
        pop_first():
            Removes and returns the value of the first node (head) in the linked list.
            Handles edge cases when the list is empty or has only one node.
            Updates head and length accordingly.
            Time Complexity: O(1)
        pop_last():
            Removes and returns the value of the last node (tail) in the linked list.
            Traverses to find the second-to-last node and updates tail pointer.
            Handles edge cases when the list is empty or has only one node.
            Time Complexity: O(n)
        prepend(value):
            Inserts a new node with the given value at the beginning of the linked list.
            Updates the head pointer and increments length.
            Time Complexity: O(1)
        get(index):
            Retrieves the node at the specified index (0-based).
            Returns None if index is out of bounds.
            Time Complexity: O(n)
        set_value(index, value):
            Updates the value of the node at the specified index.
            Returns True if successful, False if index is out of bounds.
            Time Complexity: O(n)
        insert(index, value):
            Inserts a new node with the given value at the specified index.
            Handles special cases: prepend at index 0, append at end.
            Returns True if successful, False if index is out of bounds.
            Time Complexity: O(n)
        remove(index):
            Removes and returns the value of the node at the specified index.
            Handles special cases: remove first, remove last.
            Returns None if index is out of bounds.
            Time Complexity: O(n)
        reverse():
            Reverses the entire linked list in-place by redirecting all node pointers.
            Swaps head and tail references after reversal.
            Time Complexity: O(n)
        display():
            Prints the current linked list as a list representation to the console.
            Useful for visualization and debugging.
            Time Complexity: O(n)
    """
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def add(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1
        print("Add ->", value)

    def pop_first(self):
        if self.head is None:
            return None

        temp = self.head
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            temp.next = None

        self.length -= 1
        print("Pop First ->", temp.value)
        return temp.value

    def pop_last(self):
        if self.head is None:
            return None

        temp = self.head
        pre = self.head

        if self.length == 1:
            val = self.head.value
            self.head = None
            self.tail = None
        else:
            while temp.next:
                pre = temp
                temp = temp.next
            val = temp.value
            self.tail = pre
            self.tail.next = None

        self.length -= 1
        print("Pop Last ->", val)
        return val

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        print("Prepend ->", value)

    def get(self, index):
        if index < 0 or index >= self.length:
            return None

        temp = self.head
        for _ in range(index):
            temp = temp.next

        print(f"Get Index {index} -> {temp.value}")
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            print(f"Set Index {index} -> {value}")
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            self.prepend(value)
            return True
        if index == self.length:
            self.add(value)
            return True

        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        print(f"Insert Index {index} -> {value}")
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None

        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop_last()

        prev = self.get(index - 1)
        removed = prev.next
        prev.next = removed.next
        self.length -= 1
        print(f"Remove Index {index} -> {removed.value}")
        return removed.value

    # def reverse(self):
    #     prev = None
    #     current = self.head
    #     self.tail = self.head
    #
    #     while current:
    #         next_node = current.next
    #         current.next = prev
    #         prev = current
    #         current = next_node
    #

    def reverse(self):
        prev = None
        temp = self.head
        self.tail = self.head

        for _ in range(self.length):
            next_node = temp.next
            temp.next = prev
            prev = temp
            temp = next_node

        self.head = prev
        print("Linked List Reversed")

    def display(self):
        current = self.head
        li = []
        while current:
            li.append(current.value)
            current = current.next
        print("Current list ->", li)


# ===========================
# ✅ TEST CASES
# ===========================

linked_list = LinkedList(1)
linked_list.display()   # [1]

linked_list.add(2)
linked_list.display()   # [1, 2]

linked_list.add(3)
linked_list.display()   # [1, 2, 3]

linked_list.pop_first()   # Removes 1
linked_list.display()     # [2, 3]

linked_list.pop_last()    # Removes 3
linked_list.display()     # [2]

linked_list.prepend(0)    # Adds 0 at start
linked_list.display()     # [0, 2]

linked_list.set_value(1, 5)  # Sets index 1 → 5
linked_list.display()        # [0, 5]

linked_list.remove(1)     # Removes index 1 (5)
linked_list.display()     # [0]

linked_list.insert(1, 10)  # [0, 10]
linked_list.display()

linked_list.insert(2, 6)   # [0, 10, 6]
linked_list.display()

linked_list.insert(1, 4)   # [0, 4, 10, 6]
linked_list.display()

linked_list.reverse()      # [6, 10, 4, 0]
linked_list.display()
