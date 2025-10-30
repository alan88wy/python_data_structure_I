class Node:
    """A node in a doubly linked list"""
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    """Doubly Linked List with basic insertion and palindrome check"""
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        """Add a new node at the end"""
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def is_palindrome(self):
        """Check if the linked list forms a palindrome"""
        left = self.head
        right = self.tail

        # when right move to the left of left, both crosses each other
        # so right-> is actually pointing to the new left position
        #
        # example
        #
        # 1 -> 2 -> 2 -> 1
        #      ^    ^ 
        #     left  right
        #
        # Next step
        # 1 -> 2 -> 2 -> 1
        #      ^    ^ 
        #    right  left   
        #
        # Here right.next == left, so we stop the loop because we no longer have to continue
        # It is palindrome till now, so we return True
        
        while left and right and left != right and right.next != left:
            if left.data != right.data:
                return False
            left = left.next
            right = right.prev

        return True


# --- Example Usage ---
if __name__ == "__main__":
    dll = DoublyLinkedList()
    text = input("Enter a string to check if it's a palindrome: ")

    # Build the doubly linked list (ignoring spaces and punctuation)
    for ch in text:
        if ch.isalnum():  # consider only letters/numbers
            dll.append(ch.lower())

    if dll.is_palindrome():
        print("✅ It's a palindrome!")
    else:
        print("❌ Not a palindrome.")