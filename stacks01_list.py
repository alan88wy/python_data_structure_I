"""
A stack is a linear data structure that follows the Last-In-First-Out (LIFO) principle.

Basic operations we can do on a stack are:

Push: Adds a new element on the stack.
Pop: Removes and returns the top element from the stack.
Peek: Returns the top (last) element on the stack.
isEmpty: Checks if the stack is empty.
Size: Finds the number of elements in the stack.

"""

class stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop()

    def peek(self):
        if len(self.stack) < 1:
            return None
        return self.stack[-1]

    def isEmpty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)
    
    def __str__(self):
        return str(self.stack)
    
# Example usage:
if __name__ == "__main__":     
    s = stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.pop())  # Output: 3
    print(s.peek())  # Output: 2
    print(s.isEmpty())  # Output: False
    print(s.size())