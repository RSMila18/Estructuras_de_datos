from Laboratorio_4.list import List

class OrdenadorLista:
    def __init__(self):
        self.lista = List()

    def inicializar(self, n):
        for i in range(n):
            valor = (i * 37 + 11) % 100 + 1
            self.lista.add_Last(valor)

    def ordenar(self):
        #Ordena la lista de menor a mayor usando el método de burbuja.
        if self.lista.is_Empty() == True:
            raise ValueError("La lista está vacía. No se puede ordenar.")

        size = self.lista.size()
        for i in range(size):
            current = self.lista._head
            for j in range(size - 1 - i):
                if current._data > current._next._data:  # Comparamos datos
                    # Intercambiamos los valores entre nodos
                    current._data, current._next._data = current._next._data, current._data
                current = current._next

    def mostrar(self):
        if self.lista.is_Empty() == True:
            print("La lista está vacía.")
            return

        current = self.lista._head
        elementos = []
        while current is not None:
            elementos.append(current._data)
            current = current._next
        print("Lista:", elementos)