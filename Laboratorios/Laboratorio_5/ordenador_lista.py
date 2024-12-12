from Laboratorio_4.lista_simple import List

class OrdenadorLista:
    def __init__(self):
        self.lista = List()

    def inicializar(self, n):
        for i in range(n):
            valor = (i * 37 + 11) % 100 + 1
            self.lista.add_Last(valor)

    def ordenar(self):
        # Ordena la lista de menor a mayor usando el método de burbuja.
        if self.lista.is_Empty():
            raise ValueError("La lista está vacía. No se puede ordenar.")

        size = self.lista.size()
        for i in range(size):
            current = self.lista.first()
            for j in range(size - 1 - i):
                if current.get_Data() > current.get_Next().get_Data():
                    # Intercambiamos los valores entre nodos
                    current.set_Data(
                        current.get_Next().get_Data()
                    ), current.get_Next().set_Data(current.get_Data())
                current = current.get_Next()

    def mostrar(self):
        print(self.lista)
