class SimpleStack:
    def __init__(self):
        self.stack = []  # Create an empty list to hold stack items

    def push(self, item):
        self.stack.append(item)  # Add item to the top

    def pop(self):
        if self.stack:           # Check if stack is not empty
            return self.stack.pop()  # Remove and return the top item
        else:
            return "Stack is empty!"

    def peek(self):
        if self.stack:
            return self.stack[-1]  # Return the top item without removing
        else:
            return "Stack is empty!"

    def size(self):
        return len(self.stack)  # Return number of items

    def display(self):
        print("Stack:", self.stack)  # Print stack as a list

# 🚀 Try it out!
s = SimpleStack()
s.push("A")
s.push("B")
s.push("C")

s.display()
print("Top item:", s.peek())
print("Removed:", s.pop())
s.display()
print("Total items:", s.size())