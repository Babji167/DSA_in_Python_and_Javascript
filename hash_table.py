class HashTable:
    """
    A simple hash table implementation using separate chaining for collision resolution.

    Methods:
        insert(key, value): Insert or update the value for a given key.
        get(key): Retrieve the value associated with a key, or None if not found.
        remove(key): Remove the key-value pair by key. Returns True if removed, False otherwise.
    """
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        self.table[index].append((key, value))

    def get(self, key):
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

    def remove(self, key):
        index = self._hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return True
        return False

    def __str__(self):
        result = []
        for i, bucket in enumerate(self.table):
            items = ", ".join(f"{k}: {v}" for k, v in bucket)
            result.append(f"{i}: [{items}]")
        return "\n".join(result)
    
if __name__ == "__main__":
    # Example usage and expected output for HashTable
    ht = HashTable()
    ht.insert("name", "Alice")  # Insert key 'name' with value 'Alice'
    ht.insert("age", 30)        # Insert key 'age' with value 30
    ht.insert("city", "New York")  # Insert key 'city' with value 'New York'
    
    print("Hash Table:", ht)    # Print the current state of the hash table
    
    print("Get 'name':", ht.get("name"))  # Should output: Alice
    print("Get 'age':", ht.get("age"))    # Should output: 30
    
    ht.remove("age")            # Remove the key 'age'
    print("After removing 'age':", ht)    # Print the hash table after removal
    
    print("Get 'age' after removal:", ht.get("age"))  # Should output: None