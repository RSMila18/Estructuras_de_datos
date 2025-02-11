from Laboratorios import BSTEntry

class BinarySearchTree:
    #Clase que implementa un Árbol Binario de Búsqueda.
    def __init__(self):
        self.root = None

    def insert(self, key, value):
        #Inserta un nuevo nodo en el árbol binario de búsqueda."""
        new_node = BSTEntry(key, value)
        if self.root is None:
            self.root = new_node
        else:
            self._insert_recursive(self.root, new_node)

    def _insert_recursive(self, current, new_node):
        if new_node.key < current.key:
            if current.left is None:
                current.left = new_node
            else:
                self._insert_recursive(current.left, new_node)
        else:
            if current.right is None:
                current.right = new_node
            else:
                self._insert_recursive(current.right, new_node)

    def search(self, key):
        #Busca un nodo en el árbol dado una clave."""
        return self._search_recursive(self.root, key)

    def _search_recursive(self, current, key):
        if current is None or current.key == key:
            return current
        if key < current.key:
            return self._search_recursive(current.left, key)
        return self._search_recursive(current.right, key)

    def delete(self, key):
        #Elimina un nodo del árbol dada una clave."""
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, current, key):
        if current is None:
            return current
        if key < current.key:
            current.left = self._delete_recursive(current.left, key)
        elif key > current.key:
            current.right = self._delete_recursive(current.right, key)
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
            current.right = self._delete_recursive(current.right, min_larger_node.key)
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

    def inorder_traversal(self):
        """Realiza el recorrido inorder del árbol y muestra las claves."""
        keys = []
        self._inorder_recursive(self.root, keys)
        print("Recorrido inorder:", keys)

    def _inorder_recursive(self, current, keys):
        if current:
            self._inorder_recursive(current.left, keys)
            keys.append(current.key)
            self._inorder_recursive(current.right, keys)

    def display_tree(self, node=None, level=0, prefix="Root: "):
        """Muestra visualmente el árbol."""
        if node is None:
            node = self.root
        if node is not None:
            print(" " * (level * 4) + prefix + f"({node.key}, {node.value})")
            if node.left:
                self.display_tree(node.left, level + 1, "L--- ")
            if node.right:
                self.display_tree(node.right, level + 1, "R--- ")


# Función auxiliar para calcular la clave
def calcular_clave(identificacion):
    return sum(int(digit) for digit in str(identificacion))