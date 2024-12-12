from Laboratorios.Laboratorio_4.node import Node
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
        return self._head
    
    def last(self):
        return self._tail

    def add_First(self, data):
        new_node = Node(data)
        if self.is_Empty() == True:
            self._head = self.tail = new_node
        else:
            new_node.set_Next(self._head)
            self._head = new_node
        self._size += 1

    def add_Last(self, data):
        new_node = Node(data)
        if self.is_Empty() == True:
            self._head = self._tail = new_node  
        else:
            self._tail.set_Next(new_node)
            self._tail = new_node
        self._size += 1 
        
    #No sería más bien: 
    #def add_Last(self, data):
    #    new_node = Node(data)
    #    if self.is_Empty() == True:
    #       self._head = self._tail = new_node                 ----------> En efecto, hay que cambiarlo, gracias por el aviso :D
    #    else:
    #        self.tail.set_next = new_node
    #        self.tail = new_node
    #    self.size += 1

    def remove_First(self):
        if self.is_Empty() == True:
           removed_node = self._head
           self._head = removed_node.getNext()
           removed_node.set_Next(None)
           self._size -= 1
           return removed_node.get_Data()
        else:
            return None
    
    def remove_Last(self):
        if self._size == 1:
            return self.remove_First()
        else:
            removed_node = self._tail
            anterior = self._head
            while anterior.get_Next()!= self._tail:
                anterior = anterior.get_Next()
            anterior.set_Next(None)
            self._tail = anterior
            self._size -= 1
            return removed_node.get_Data()