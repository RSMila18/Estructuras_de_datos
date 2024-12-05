from Laboratorio_4.node import Node
class List:
    def __init__(self, head = None, tail = None, size = 0):
        self._head = head
        self._tail = tail
        self._size = size

    def size(self):
        return self._size

    def is_Empty(self):
        if self._size == 0:
            return True
        else:
            return False

    def set_Size(self, size):
        self._size = size

    def first(self):
        if self.is_empty() == True:
            raise ValueError("Lista vacia")
        return self._head
    
    def last(self):
        if self.is_empty() == True:
            raise ValueError("Lista vacia")
        return self._tail

    def add_First(self, data):
        new_node = Node(data)
        if self.is_empty() == True:
            self._head = self.tail = new_node
        else:
            new_node._next = self.head
            self._head = new_node
        self._size += 1

    def add_Last(self, data):
        new_node = Node(data)
        if self.is_empty() == True:
            self._head = self._tail = new_node  
            self._tail._next = new_node  
            self._tail = new_node
        self._size += 1 

    def remove_First(self):
        if self.is_empty() == True:
            raise ValueError("Lista vacia")
        data = self.head.data
        self.head = self.head.next
        self.size -= 1
        return data
