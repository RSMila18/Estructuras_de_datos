class BinaryTree:
    
    def __init__(self):
        self.root = None
        self.size = 0

    def size(self):
        return self.size

    def is_empty(self):  
        return self.root is None
    
    def Isroot(self, node):
        return self.root == node
    
    def isInternal(self, node):
        return node.left is not None or node.right is not None

    def has_left(self, node):
        return node.left is not None
    
    def has_right(self, node):
        return node.right is not None
    
    def depth(self, doublenode):
        if doublenode == self.root:
            return 0
        else:
            return 1 + self.depth(doublenode.parent)
        
    def height(self, node):
        if node is None:
            return 0
        else:
            return 1 + max(self.height(node.left), self.height(node.right))
    
    def root(self):
        return self.root
    
    def left(self, node):   
        return node.getleft()
    
    def right(self, node):
        return node.getright()
    
    def parent(self, node):
        if self.Isroot(node):
            return None
        else:
            return node.parent
        
    def add_root(self, e):
        self.size = 1
        self.root = e

    def insert_left(self, node, e):
        self.size += 1
        node.left = e
        e.parent = node

    def insert_right(self, node, e):
        self.size += 1
        node.right = e
        e.parent = node
    

    def display_tree(self, node=None, level=0, prefix="Root: "):
        if node is None:
            node = self.root
        if node is not None:
            print(" " * (level * 4) + prefix + f"({node.key}, {node.value})")
            if node.left:
                self.display_tree(node.left, level + 1, "L--- ")
            if node.right:
                self.display_tree(node.right, level + 1, "R--- ")