class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
            new_node.prev = current
        self.length += 1
        return True

    def print_list(self):
        values = []
        temp = self.head
        while temp is not None:
            values.append(str(temp.value))
            temp = temp.next
        result = " -> ".join(values) if values else "Empty"
        print(result + " -> None")
        return result

    def make_empty(self):
        self.head = None
        self.length = 0

    def reverse_between(self, start_index, end_index):
        #   +===================================================+
        #   |               WRITE YOUR CODE HERE                |
        #   | Description:                                      |
        #   | - Reverses a segment of a doubly linked list      |
        #   |   between the given start_index and end_index.    |
        #   | - This operation modifies only the segment in     |
        #   |   place, preserving the rest of the list.         |
        #   |                                                   |
        #   | Behavior:                                         |
        #   | - A dummy node is used to simplify edge cases     |
        #   |   like reversing from the head.                   |
        #   | - The `prev` pointer moves to the node before     |
        #   |   the reversal section.                           |
        #   | - The segment is reversed by removing nodes one   |
        #   |   at a time and reinserting them at the front of  |
        #   |   the sublist.                                    |
        #   | - All `next` and `prev` pointers are updated      |
        #   |   carefully to maintain list integrity.           |
        #   | - At the end, the new head is set properly and    |
        #   |   its prev pointer is cleared.                    |
        #   +===================================================+
   
        if not self.head or self.head.next is None:
            # If the list is empty or has only one node, no reversal is needed.
            return True 
        
        if start_index < 0 or end_index >= self.length or start_index > end_index:
            return False
        
        # 2. If m == n, no reversal needed
        if start_index == end_index:
            return True
        
        print("start_index:", start_index, "end_index:", end_index)
        dummy = Node(0)
        dummy.next = self.head
        self.head.prev = dummy

        pre_node = dummy
        
        for _ in range(start_index):
            pre_node = pre_node.next

        start_node = pre_node.next
        current = start_node
        prev = None

        for _ in range(end_index - start_index + 1):
            next_node = current.next
            current.next = prev
            current.prev = next_node
            prev = current
            current = next_node
        
        # Reconnect the reversed sublist with the rest of the list
        pre_node.next = prev
        prev.prev = pre_node
        start_node.next = current
        
        if current:
            current.prev = start_node
            
        self.head = dummy.next
        self.head.prev = None
    
        return True
    
        
        
        

    def reverse(self, head):
        prev = None
        current = head

        while current is not None:
            next_node = current.next
            current.next = prev
            current.prev = next_node
            prev = current
            current = next_node

        return prev
            







# Test Cases
print("\nTest 1: Middle segment reversal")
dll1 = DoublyLinkedList(3)
for v in [8, 5, 10, 2, 1]:
    dll1.append(v)
print("BEFORE: ", end="")
dll1.print_list()
dll1.reverse_between(1, 4)
print("AFTER:  ", end="")
dll1.print_list()

print("\nTest 2: Full list reversal")
dll2 = DoublyLinkedList(1)
for v in [2, 3, 4, 5]:
    dll2.append(v)
print("BEFORE: ", end="")
dll2.print_list()
dll2.reverse_between(0, 4)
print("AFTER:  ", end="")
dll2.print_list()

print("\nTest 3: No-op on single node")
dll3 = DoublyLinkedList(9)
print("BEFORE: ", end="")
dll3.print_list()
dll3.reverse_between(0, 0)
print("AFTER:  ", end="")
dll3.print_list()

print("\nTest 4: Reversal with head involved")
dll4 = DoublyLinkedList(7)
for v in [8, 9]:
    dll4.append(v)
print("BEFORE: ", end="")
dll4.print_list()
dll4.reverse_between(0, 2)
print("AFTER:  ", end="")
dll4.print_list()

