from Laboratorios.Laboratorio_4.doble_node import DoubleNode

class DoubleList:
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

    def first(self):
        if self.is_Empty() == True:
            raise ValueError("Lista vacia")
        return self._head

    def last(self):
        if self.is_Empty() == True:
            raise ValueError("Lista vacia")
        return self._tail

    def add_first(self, data):
        new_node = DoubleNode(data)
        if self.is_Empty() == True:
            self._head = self._tail = new_node
        else:
            new_node.next = self._head
            self._head.prev = new_node
            self._head = new_node
        self._size += 1

    def add_last(self, data):
        new_node = DoubleNode(data)
        if self.is_Empty() == True:
            self._head = self._tail = new_node
        else:
            self._tail.next = new_node
            new_node.prev = self._tail
            self._tail = new_node
        self._size += 1

    def remove_first(self):
        if self.is_Empty() == True:
            raise ValueError("Lista vacia")
        removed_node = self._head
        if self._size == 1:  # Si hay solo un nodo
            self._head = self._tail = None
        else:
            self._head = self._head.next
            self._head.prev = None
        self._size -= 1
        return removed_node.data

    def remove_last(self):
        if self.is_Empty() == True:
            raise ValueError("Lista vacia")
        removed_node = self._tail
        if self._size == 1:  # Si hay solo un nodo
            self._head = self._tail = None
        else:
            self._tail = self._tail.prev
            self._tail.next = None
        self._size -= 1
        return removed_node.data

    def remove(self, node):
        if self.is_Empty() == True:
            raise ValueError("Lista vacia")
        if node is self._head:
            return self.remove_first()
        elif node is self._tail:
            return self.remove_last()
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            self._size -= 1
            return node.data

    def add_after(self, node, data):
        if node is None:
            raise ValueError("El nodo de referencia no puede ser None")
        if node is self._tail:  # Si es el último nodo
            self.add_last(data)
        else:
            new_node = DoubleNode(data)
            new_node.next = node.next
            new_node.prev = node
            node.next.prev = new_node
            node.next = new_node
            self._size += 1

    def add_before(self, node, data):
        if node is None:
            raise ValueError("El nodo de referencia no puede ser None")
        if node is self._head:  # Si es el primer nodo
            self.add_first(data)
        else:
            new_node = DoubleNode(data)
            new_node.next = node
            new_node.prev = node.prev
            node.prev.next = new_node
            node.prev = new_node
            self._size += 1