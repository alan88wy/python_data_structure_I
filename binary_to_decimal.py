class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def binary_to_decimal(head: ListNode) -> int:
    num = 0
    current = head
    
    while current:
        num = num * 2 + current.val
        current = current.next
        
    return num


# Example usage:
# Binary: 1 -> 0 -> 1  (represents 5 in decimal)

head = ListNode(1)
head.next = ListNode(0)
head.next.next = ListNode(1)
head.next.next.next = ListNode(1)

print(binary_to_decimal(head))  # Output: 5