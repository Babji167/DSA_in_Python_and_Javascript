class Node:
    """
    A class representing a node in a binary tree, with data and left/right children.
    """
    def __init__(self, data): 
        self.data=data 
        self.right=None
        self.left=None

    def insert_left(self,data):
        node = Node(data)
        if self.get_left_child() is None:
            self.set_left_child(node)
        else:
            node.set_left_child(self.get_left_child())
            self.set_left_child(node)

    def insert_right(self,data):
        node = Node(data)
        if self.get_right_child() is None:
            self.set_right_child(node)
        else:
            node.set_right_child(self.get_right_child())
            self.set_right_child(node)

    def set_left_child(self, node):
        self.left = node

    def set_right_child(self, node):
        self.right = node

    def get_left_child(self):
        return self.left
    
    def get_right_child(self):
        return self.right
    
    def get_data(self):
        return self.data
    
    def __str__(self):
        return str(self.data)


    def __repr__(self):
        return f"Node({self.data})"
    

def create_tree() -> Node:
    """
    Creates a simple binary tree with a root node and left/right children.
    Returns the root node of the constructed tree.
    """
    root = Node(1)
    root.insert_left(2)
    root.insert_right(3)
    
    left_child = root.get_left_child()
    left_child.insert_left(4)
    left_child.insert_right(5)
    
    right_child = root.get_right_child()
    right_child.insert_left(6)
    right_child.insert_right(7)
    
    return root
    
def print_tree_preorder(node):
    if node is not None:
        print(node.data, end=' ')
        print_tree_preorder(node.get_left_child())
        print_tree_preorder(node.get_right_child())

if __name__ == "__main__":
    tree = create_tree()
    print_tree_preorder(tree)
    print()  # for newline after printing






    
