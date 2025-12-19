class TrieNode:
    def __init__(self):
        # Dictionary to hold children: letter → TrieNode
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word.lower():  # Convert to lowercase
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end_of_word = True  # Mark end of the word

    def search(self, word):
        node = self.root
        for ch in word.lower():
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_end_of_word

# Test the Trie
my_trie = Trie()
my_trie.insert("python")
my_trie.insert("java")

print(my_trie.search("python"))  # True
print(my_trie.search("java"))    # True
print(my_trie.search("csharp"))  # False