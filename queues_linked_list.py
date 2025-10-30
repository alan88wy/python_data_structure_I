"""
A queue is a linear data structure that follows the First-In-First-Out (FIFO) principle.

Queues
Think of a queue as people standing in line in a supermarket.

The first person to stand in line is also the first who can pay and leave the supermarket.

Basic operations we can do on a queue are:

1. Enqueue: Adds a new element to the queue.
2. Dequeue: Removes and returns the first (front) element from the queue.
3. Peek: Returns the first element in the queue.
4. isEmpty: Checks if the queue is empty.
5. Size: Finds the number of elements in the queue.

Queues can be implemented by using arrays or linked lists.

Queues can be used to implement job scheduling for an office printer, order processing 
for e-tickets, or to create algorithms for breadth-first search in graphs.
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def isEmpty(self):
        return self.front is None

    def enqueue(self, value):
        new_node = Node(value)
        if self.isEmpty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
            
        self.size += 1

    def dequeue(self):
        if self.isEmpty():
            return None
        else:
            value = self.front.value
            self.front = self.front.next
            self.size -= 1
            
            if self.isEmpty():
                self.rear = None
                
            return value

    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.front.value

    def size(self):
        return self.size    # end class Queue
    
# Example usage:
queue = Queue() # Create a new queue
queue.enqueue(1)  # Add 1 to the queue
queue.enqueue(2)  # Add 2 to the queue
print(queue.peek())  # Print the front element of the queue (1)
print(queue.dequeue())  # Remove and print the front element of the queue (1)


# end class Node