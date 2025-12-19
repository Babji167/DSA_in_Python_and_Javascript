class SimpleHashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        return key % self.size
    
    def insert(self, key, value):
        index = self._hash(key)
        self.table[index] = (key, value)

    def get(self, key):
        index = self._hash(key)
        if self.table[index] and self.table[index][0] == key:
            return self.table[index][1]
        return None

ht = SimpleHashTable()
ht.insert(103, "Alice")
ht.insert(115, "Bob")
ht.insert(120, "Stark")

print(ht.get(103))  # Outputs: Alice
print(ht.get(120))  # Outputs: Stark
print(ht.get(999))  # Outputs: None (not found)