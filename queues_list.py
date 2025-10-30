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

class Queue:
  def __init__(self):
    self.queue = []
    
  def enqueue(self, element):
    self.queue.append(element)

  def dequeue(self):
    if self.isEmpty():
      return "Queue is empty"
    return self.queue.pop(0)

  def peek(self):
    if self.isEmpty():
      return "Queue is empty"
    return self.queue[0]

  def isEmpty(self):
    return len(self.queue) == 0

  def size(self):
    return len(self.queue)

# Create a queue
myQueue = Queue()

myQueue.enqueue('A')
myQueue.enqueue('B')
myQueue.enqueue('C')

print("Queue: ", myQueue.queue)
print("Peek: ", myQueue.peek())
print("Dequeue: ", myQueue.dequeue())
print("Queue after Dequeue: ", myQueue.queue)
print("isEmpty: ", myQueue.isEmpty())
print("Size: ", myQueue.size())