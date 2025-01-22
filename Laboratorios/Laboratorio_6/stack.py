from Laboratorio_4.lista_simple import List

class Stack:
    def __init__(self):
        self.data = List()
        
    def size(self):
        return self.data.size()
    
    def isEmpty(self):
        return self.data.is_Empty()
    
    def push(self, data):
        self.data.add_First(data)
    
    def pop(self):
        if self.isEmpty():
            print("La pila está vacía")
            return None
        else:
            return self.data.remove_First()
        
    def top(self):
        if self.isEmpty():
            print("La pila está vacía")
            return None
        else:
            return self.data.first()
        
    def __str__(self):
        return self.data.__str__()