class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head
        self.length = 1

    def append(self, value):
        
        print("append -> ", value)
        
        new_node = Node(value)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node    
            self.length += 1
            
        return True
    
    def pop(self):
        
        print("pop -> ", self.tail.value)
        
        if self.length == 0:
            return None
        
        temp = self.tail
        
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
            
        self.length -= 1
        
        if self.length == 0:
            self.head = None
            self.tail = None
            
        return temp
    
    def pop_last(self):
        
        print("pop_last -> ", self.head.value)
        
        if self.length == 0:
            return None
        
        temp = self.head
        
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
            
        self.length -= 1
        return temp
    
    def remove(self, value)    :
        
        print("remove -> ", value)
        
        if self.length == 0:
            return None
        
        current = self.head
        
        while current is not None:
            if current.value == value:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                    
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                self.length -= 1
                
                return current
            
            current = current.next  
            
        return None
        
    def prepend(self, value):
        
        print("prepend -> ", value)
        
        new_node = Node(value)
        
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            
        self.length += 1
        
        return True  

    def print_list(self):

        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0
         
    def reverse(self):
        print("reverse -> ")
        
        if self.length == 0:
            return

        current = self.head
        self.head = self.tail
        self.tail = current

        while current is not None:
            current.prev, current.next = current.next, current.prev
            # The above will be the same as below
            # temp = current.prev
            # current.prev = current.next
            # current.next = temp
            
            current = current.prev  # Move to the next node in the original order 
        return True 
    
    def swap_pairs(self):
        print("Swap Pairs -> ")
        
        if self.length < 2:
            return
        
        current = self.head
        
        while current and current.next:
            # Swap values of current node and next node
            current.value, current.next.value = current.next.value, current.value
            
            # Move to the next pair
            current = current.next.next
            
        return True
    
    def partition_list(self, x):
        
        print("Partition List -> ")
        
        if self.head is None:
            return
        
        dummy1 = Node(0)  # Dummy node for the list of nodes < x
        dummy2 = Node(0)  # Dummy node for the list of nodes >= x
        
        prev1 = dummy1  # Pointer to the last node in the < x list
        prev2 = dummy2  # Pointer to the last node in the >= x list
        
        current = self.head
        
        while current is not None:
            if current.value < x:
                prev1.next = current
                current.prev = prev1
                prev1 = prev1.next
            else:
                prev2.next = current
                current.prev = prev2
                prev2 = prev2.next
            current = current.next
        
        # Terminate the two lists
        prev1.next = dummy2.next
        if dummy2.next is not None:
            dummy2.next.prev = prev1
        prev2.next = None
        
        # Update head and tail of the doubly linked list
        self.head = dummy1.next
        if self.head is not None:
            self.head.prev = None
        
        self.tail = prev2 if prev2 != dummy2 else prev1
        
        return True
    
    def reverse_between(self, m, n):
        
        print(f"Reverse Between {m} and {n} -> ")
        
        if self.head is None or m >= n or m < 0 or n >= self.length:
            return
        
        dummy = Node(0)
        dummy.next = self.head
        if self.head:
            self.head.prev = dummy
        
        pre_node = dummy
        
        for _ in range(m):
            pre_node = pre_node.next
        
        start_node = pre_node.next
        current = start_node
        prev = None 
        
        for _ in range(n - m + 1):
            next_node = current.next
            current.next = prev
            if prev:
                prev.prev = current
            prev = current
            current = next_node
        
        pre_node.next = prev
        if prev:
            prev.prev = pre_node
        
        start_node.next = current
        if current:
            current.prev = start_node
        
        self.head = dummy.next
        if self.head:
            self.head.prev = None
        
        return True
    
def run():
    # Example usage:
    
    print("create -> 3")
    dll = DoublyLinkedList(3)
    dll.append(1)
    dll.append(4)
    dll.append(2)
    dll.append(5)
    print("Initial list -> ")
    dll.print_list()
    dll.partition_list(3)
    dll.print_list()
    p = dll.pop()
    dll.print_list()
    p = dll.pop_last()
    dll.print_list()
    dll.remove(4)
    dll.print_list()
    dll.prepend(0)
    dll.print_list()
    dll.swap_pairs() 
    dll.print_list()
    dll.reverse()
    dll.print_list()
    dll.reverse_between(1,2)
    dll.print_list()

    
    
if __name__ == "__main__":
    run()
