class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def size(self):
        return len(self.items)

    def __str__(self):
        return "Current Stack: [" + ", ".join(str(x) for x in self.items) + "]"

if __name__ == "__main__":
    s = Stack()
    s.push("Babji")
    s.push("Alice")
    s.push("Charlie")
    s.push("Diana")
    s.push("Stark")

    print(s)
    print("Top:", s.peek())
    print("Popped:", s.pop())
    print("Top:", s.peek())
    print("Popped:", s.pop())
    print(s)
    print("Total in stack:", s.size())
