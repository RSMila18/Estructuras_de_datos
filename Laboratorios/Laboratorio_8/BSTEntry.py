class BSTEntry:
    #Clase que representa una entrada en el árbol binario de búsqueda."""
    def __init__(self, key, value):
        self.key = key  # Clave entera
        self.value = value  # Datos genéricos
        self.left = None  # Hijo izquierdo
        self.right = None  # Hijo derecho
