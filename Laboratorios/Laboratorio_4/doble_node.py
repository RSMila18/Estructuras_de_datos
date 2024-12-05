class DoubleNode:
    def __init__(self, data = None, _next = None, prev = None):
        self._data = data
        self._next = _next
        self._prev = prev

    def set_Data(self, object_):
        self._data = object_
    
    def set_Next(self, DoubleNode):
        self._next = DoubleNode

    def set_Prev(self, DoubleNode):
        self._prev = DoubleNode
    
    def get_Data(self):
        return self._data
    
    def get_Next(self):
        return self._next
    
    def get_prev(self):
        return self._prev
