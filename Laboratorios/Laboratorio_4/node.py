class Node:
    def __init__(self, data=None, node = None):
        self._data = data
        self._next = node
    def set_Data(self, Object):
        self._data = Object
    
    def set_Next(self, Node):
        self._next = Node
    
    def get_Data(self):
        return self._data
    
    def get_Next(self):
        return self._next
    