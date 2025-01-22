from Laboratorio_4.lista_simple import List

class Queue:
    def __init__(self):
        self.data = List()
        
    def size(self):
        return self.data.Size()
    
    def isEmpty(self):
        return self.data.is_Empty()
    
    def enqueue(self, object):
        self.data.add_Last(object)
    
    def dequeue(self):
        return self.data.remove_First()
        
    def First(self):
        return self.data.first()