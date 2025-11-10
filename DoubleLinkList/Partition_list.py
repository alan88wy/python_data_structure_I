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

    def print_list(self):
        output = []
        current_node = self.head
        while current_node is not None:
            output.append(str(current_node.value))
            current_node = current_node.next
        print(" <-> ".join(output))
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
        self.length += 1
        return True

    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0

        
    def partition_list(self, x):
        #   +===================================================+
        #   |               WRITE YOUR CODE HERE                |
        #   | Description:                                      |
        #   | - Partitions a doubly linked list around a value  |
        #   |   `x`.                                            |
        #   | - All nodes with values less than `x` come before |
        #   |   nodes with values greater than or equal to `x`. |
        #   |                                                   |
        #   | Behavior:                                         |
        #   | - Uses two dummy nodes to create two sublists:    |
        #   |   one for nodes < x, and one for nodes >= x.      |
        #   | - Each node is added to the appropriate sublist   |
        #   |   while maintaining both next and prev pointers.  |
        #   | - The sublists are then joined together.          |
        #   | - The head of the list is updated to the start of |
        #   |   the merged result.                              |
        #   +===================================================+
        if self.head is None:
            return

        dummy1 = Node(0)
        dummy2 = Node(0)
        prev1 = dummy1
        prev2 = dummy2
        curr = self.head

        while curr:
            if curr.value < x:
                prev1.next = curr
                prev1 = curr
            else:
                prev2.next = curr
                prev2 = curr
                
            curr = curr.next

        prev1.next = dummy2.next
        prev2.next = None
        self.head = dummy1.next
        # Update prev pointers
        if self.head:
            self.head.prev = None
            curr = self.head.next
            prev = self.head
            
            while curr:
                curr.prev = prev
                prev = curr
                curr = curr.next
                

    
# -------------------------------
# Test Cases:
# -------------------------------

print("\nTest Case 1: Partition around 5")
dll1 = DoublyLinkedList(3)
dll1.append(8)
dll1.append(5)
dll1.append(10)
dll1.append(2)
dll1.append(1)
print("BEFORE: ", end="")
dll1.print_list()
dll1.partition_list(5)
print("AFTER:  ", end="")
dll1.print_list()

print("\nTest Case 2: All nodes less than x")
dll2 = DoublyLinkedList(1)
dll2.append(2)
dll2.append(3)
print("BEFORE: ", end="")
dll2.print_list()
dll2.partition_list(5)
print("AFTER:  ", end="")
dll2.print_list()

print("\nTest Case 3: All nodes greater than x")
dll3 = DoublyLinkedList(6)
dll3.append(7)
dll3.append(8)
print("BEFORE: ", end="")
dll3.print_list()
dll3.partition_list(5)
print("AFTER:  ", end="")
dll3.print_list()

print("\nTest Case 4: Empty list")
dll4 = DoublyLinkedList(1)
dll4.make_empty()
print("BEFORE: ", end="")
dll4.print_list()
dll4.partition_list(5)
print("AFTER:  ", end="")
dll4.print_list()

print("\nTest Case 5: Single node")
dll5 = DoublyLinkedList(1)
print("BEFORE: ", end="")
dll5.print_list()
dll5.partition_list(5)
print("AFTER:  ", end="")
dll5.print_list()

