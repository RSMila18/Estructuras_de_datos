class BinaryTree:
    """Clase base para un Árbol Binario."""
    def __init__(self):
        self.root = None

    def is_empty(self):
        """Verifica si el árbol está vacío."""
        return self.root is None

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