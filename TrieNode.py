class TrieNode: #class for each node in the Trie
    """A node in the Trie data structure."""
    def __init__(self):
        self.children = [None]*26 # 26 letters in the English alphabet
        self.end_of_key = False # end_of_key indicates if the node marks the end of a valid key

class Trie: #class for the Trie data structure
    def __init__(self):
        self.root = TrieNode() # root node of the Trie

    @staticmethod # function to convert character to index
    def char_to_index(ch):
        if not ('a' <= ch <= 'z'): # check if character is a lowercase letter
            raise ValueError(f"Invalid character '{ch}': must be a lowercase letter a-z") #  raise error if not
            # Convert character to index (0 for 'a', 1 for 'b', ...,
        return ord(ch) - ord('a')  # ord('a') is 97, so 'a' becomes 0, 'b' becomes 1, etc.
    def insert(self,key): # insert a key into the Trie
        key=key.lower() # convert key to lowercase
        current_node = self.root  # start from the root node
        # Traverse the Trie for each character in the key
        for i in range(len(key)): # loop through each character in the key
            # Convert character to index
            index = self.char_to_index(key[i])
            if current_node.children[index] is None: # if the child node does not exist, create a new TrieNode
                current_node.children[index] = TrieNode() # create a new TrieNode
            # Move to the child node
            current_node = current_node.children[index] # update current_node to the child node
        # Mark the end of the key
        
        current_node.end_of_key = True # mark the current node as the end of a valid key

    def search(self, key):  # search for a key in the Trie
        """Search for a key in the Trie."""
        key = key.lower() # convert key to lowercase
        current_node = self.root # start from the root node
        for i in range(len(key)): # loop through each character in the key
            index = self.char_to_index(key[i]) # convert character to index
            if current_node.children[index] is None: # if the child node does not exist, the key is not present
                return False
            current_node = current_node.children[index] # move to the child node 
        # If we reach here, the key is present if current_node marks the end of a valid key
        # Return True if the current node marks the end of a valid key
        
        return current_node is not None and current_node.end_of_key
    
if __name__ == "__main__": # main function to test the Trie implementation
    # Example usage of the Trie data structure
    keys =["python", "java", "javascript", "csharp", "pascal", "pyflakes", "perl"]  # list of keys to insert into the Trie
    trie = Trie() 
    for key in keys:
        trie.insert(key) # insert each key into the Trie
    
    f_dict = { True: "Found", False: "Not Found" } # dictionary to map boolean results to strings for output

    search_keys = ["python", "perl", "go"] # keys to search in the Trie

    for key in search_keys: # search each key in the Trie
        print("key {} is {} in trie".format(key, f_dict[trie.search(key)])) # output whether the key is found or not in the Trie
