class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        """
        Removes and returns the front item of the queue.
        Returns None if the queue is empty.
        """
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def peek(self):
        """
        Returns the item at the front of the queue without removing it.
        Returns None if the queue is empty.
        """
        if not self.is_empty():
            return self.items[0]
        return None

    def size(self):
        return len(self.items)

    def __str__(self):
        return "Queue: [" + ", ".join(str(item) for item in self.items) + "]"

if __name__ == "__main__":
    # Example usage and expected output for Queue
    q = Queue()
    q.enqueue(1)  # Enqueue 1
    q.enqueue(2)  # Enqueue 2
    q.enqueue(3)  # Enqueue 3

    print("Queue after enqueuing:", q)  # Should output: Queue: [1, 2, 3]

    print("Dequeue:", q.dequeue())  # Should output: 1
    print("Queue after dequeue:", q)  # Should output: Queue: [2, 3]

    print("Peek:", q.peek())  # Should output: 2 (the next item to be dequeued)

    print("Queue size:", q.size())  # Should output: 2 (size of the queue)

    q.dequeue()  # Dequeue another item
    print("Queue after another dequeue:", q)  # Should output: Queue: [3]