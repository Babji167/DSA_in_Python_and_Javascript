class EasyQueue:
    def __init__(self):
        # Start with an empty list to hold items
        self.line = []

    def is_empty(self):
        # Check if the line is empty
        return len(self.line) == 0

    def add(self, item):
        # Add item to the end of the line
        self.line.append(item)

    def remove(self):
        # Remove the first item (front of the line)
        if not self.is_empty():
            return self.line.pop(0)
        else:
            return None  # Nothing to remove if empty

    def front(self):
        # Just look at the first item without removing
        if not self.is_empty():
            return self.line[0]
        else:
            return None

    def count(self):
        # Return how many items are in the line
        return len(self.line)

    def __str__(self):
        # Nicely format the queue for printing
        return "Current Line: [" + ", ".join(str(x) for x in self.line) + "]"

# 🚀 Try it out!
if __name__ == "__main__":
    q = EasyQueue()
    q.add("Babji")
    q.add("Alice")
    q.add("Charlie")

    print(q)                  # Shows full line
    print("Front:", q.front())  # Who's next?
    print("Removed:", q.remove())  # Serve the first
    print(q)                  # Updated line
    print("Total in line:", q.count())