class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
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

    # WRITE REVERSE_BETWEEN METHOD HERE #
    #                                   #
    #                                   #
    #                                   #
    #                                   #
    #####################################
    def reverse_between(self, m, n):
        # 0. Handle edge cases for empty or single-node list
        if not self.head or self.head.next is None:
            # If the list is empty or has only one node, no reversal is needed.
            return True 

        # 1. Validate indices: m and n are 0-indexed.
        # n must be strictly less than self.length as it refers to an existing index.
        # m must be less than or equal to n.
        if m < 0 or n >= self.length or m > n:
            return False

        # 2. If m == n, no reversal needed
        if m == n:
            return True

        # 3. Create a dummy node to simplify handling cases where m = 0 (reversing from head)
        dummy = Node(0)
        dummy.next = self.head
        
        # 4. Find the node immediately *before* the sublist to be reversed.
        # This will be `pre_node`.
        pre_node = dummy
        
        for _ in range(m):
            pre_node = pre_node.next

        # `start_node` is the first node of the sublist to be reversed (original node at index m).
        start_node = pre_node.next
        
        # `current` will be used to iterate through the sublist to reverse.
        # `prev` will be used to reverse pointers and will become the new head of the reversed sublist.
        current = start_node
        prev = None 
        
        # 5. Reverse the sublist from m to n.
        # We need to reverse (n - m + 1) nodes.
        for _ in range(n - m + 1):
            next_node = current.next   # Store the next node in the original list
            current.next = prev        # Reverse current node's pointer
            prev = current             # Move prev to the current node (building the reversed list)
            current = next_node        # Move current to the next original node
        
        # After the loop:
        # - `prev` points to the new head of the reversed sublist (the node originally at index n).
        # - `current` points to the node immediately *after* the reversed sublist (the node originally at index n+1).
        # - `start_node` points to the original head of the sublist (the node originally at index m),
        #   which now becomes the tail of the reversed sublist.

        # 6. Connect the three parts of the list:
        #    a. The node *before* the sublist (`pre_node`) points to the new head of the reversed sublist (`prev`).
        pre_node.next = prev
        
        #    b.  start_node (the original head of the sublist) which now becomes the tail of the reversed sublist,
        #        The new *tail* of the reversed sublist (`start_node`) points to the node *after* the sublist (`current`).
        start_node.next = current

        # 7. Update the head of the main linked list.
        # If m was 0, `pre_node` was `dummy`, so `dummy.next` is now the new head.
        self.head = dummy.next
        
        return True

linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)

print("Original linked list: ")
linked_list.print_list()

# Reverse a sublist within the linked list
linked_list.reverse_between(2, 4)
print("Reversed sublist (2, 4): ")
linked_list.print_list()

# Reverse another sublist within the linked list
linked_list.reverse_between(0, 4)
print("Reversed entire linked list: ")
linked_list.print_list()

# Reverse a sublist of length 1 within the linked list
linked_list.reverse_between(3, 3)
print("Reversed sublist of length 1 (3, 3): ")
linked_list.print_list()

# Reverse an empty linked list
empty_list = LinkedList(0)
empty_list.make_empty()
empty_list.reverse_between(0, 0)
print("Reversed empty linked list: ")
empty_list.print_list()


"""
    EXPECTED OUTPUT:
    ----------------
    Original linked list: 
    1 -> 2 -> 3 -> 4 -> 5 -> None
    Reversed sublist (2, 4): 
    1 -> 2 -> 5 -> 4 -> 3 -> None
    Reversed entire linked list: 
    3 -> 4 -> 5 -> 2 -> 1 -> None
    Reversed sublist of length 1 (3, 3): 
    3 -> 4 -> 5 -> 2 -> 1 -> None
    Reversed empty linked list: 
    Empty -> None
    
"""
