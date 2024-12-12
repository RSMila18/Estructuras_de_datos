class Node:
    def __init__(self, data=None, node = None):
        self._data = data
        self._next = node
        
    def set_Data(self, Object):
        self._data = Object
    
    def set_Next(self, node):  #Aquí python dice que no le gusta ese Node con N mayúscula y que sería bonito si se cambia, no sé qué opinan ustedes :)/Se cambia y ya xd, no es mucho problema
        self._next = node
    
    def get_Data(self):
        return self._data
    
    def get_Next(self):
        return self._next
    