from Laboratorio_8.BSTEntry import BSTEntry
class BinarySearchTree:
    #Clase que implementa un Árbol Binario de Búsqueda.
    def __init__(self):
        self.root = None

    def insertar(self, key, value):
        #Inserta un nuevo nodo en el árbol binario de búsqueda."""
        new_node = BSTEntry(key, value)
        if self.root is None:
            self.root = new_node
        else:
            self.insertar_recursivo(self.root, new_node)

    def insertar_recursivo(self, current, new_node):
        if new_node.key < current.key:
            if current.left is None:
                current.left = new_node
            else:
                self.insertar_recursivo(current.left, new_node)
        else:
            if current.right is None:
                current.right = new_node
            else:
                self.insertar_recursivo(current.right, new_node)

    def Buscar(self, key):
        #Busca un nodo en el árbol dado una clave."""
        return self.Busqueda_recursiva(self.root, key)

    def Busqueda_recursiva(self, current, key):
        if current is None or current.key == key:
            return current
        if key < current.key:
            return self.Busqueda_recursiva(current.left, key)
        return self.Busqueda_recursiva(current.right, key)

    def Eliminar(self, key):
        #Elimina un nodo del árbol dada una clave."""
        self.root = self._delete_recursive(self.root, key)

    def Eliminacion_recursiva(self, current, key):
        if current is None:
            return current
        if key < current.key:
            current.left = self.Eliminacion_recursiva(current.left, key)
        elif key > current.key:
            current.right = self.Eliminacion_recursiva(current.right, key)
        else:
            # Caso 1: Nodo sin hijos
            if current.left is None and current.right is None:
                return None
            # Caso 2: Nodo con un solo hijo
            if current.left is None:
                return current.right
            if current.right is None:
                return current.left
            # Caso 3: Nodo con dos hijos
            min_larger_node = self._get_min(current.right)
            current.key = min_larger_node.key
            current.value = min_larger_node.value
            current.right = self.Eliminacion_recursiva(current.right, min_larger_node.key)
        return current

    def get_min(self):
        #Obtiene el nodo con la clave más pequeña."""
        if self.root is None:
            return None
        return self._get_min(self.root).value

    def _get_min(self, current):
        while current.left is not None:
            current = current.left
        return current

    def get_max(self):
        #Obtiene el nodo con la clave más grande."""
        if self.root is None:
            return None
        current = self.root
        while current.right is not None:
            current = current.right
        return current.value

    def Recorrido_Inorder(self):
        """Realiza el recorrido inorder del árbol y muestra las claves."""
        keys = []
        self._inorder_recursive(self.root, keys)
        print("Recorrido inorder:", keys)

    def Recorrido_Inorder_recursivo(self, current, keys):
        if current:
            self.Recorrido_Inorder_recursivo(current.left, keys)
            keys.append(current.key)
            self.Recorrido_Inorder_recursivo(current.right, keys)

    def Mostrar_Arbol(self, node=None, level=0, prefix="Root: "):
        """Muestra visualmente el árbol."""
        if node is None:
            node = self.root
        if node is not None:
            print(" " * (level * 4) + prefix + f"({node.key}, {node.value})")
            if node.left:
                self.Mostrar_Arbol(node.left, level + 1, "L--- ")
            if node.right:
                self.Mostrar_Arbol(node.right, level + 1, "R--- ")


# Función auxiliar para calcular la clave
def calcular_clave(identificacion):
    return sum(int(digit) for digit in str(identificacion))