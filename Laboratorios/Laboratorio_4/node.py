class Node:
    def __init__(self, data=None, node = None):
        self.data = data
        self.next = node
    def set_Data(self, Object):
        self.data = Object
    
    def set_Next(self, Node):
        self.next = Node
    
    def get_Data(self):
        return self.data
    
    def get_Next(self):
        return self.next
    