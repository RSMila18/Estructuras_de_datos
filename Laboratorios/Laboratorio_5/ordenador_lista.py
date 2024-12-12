import random
from Laboratorio_4.lista_simple import List

class OrdenadorLista:
    def __init__(self):
        self.lista = List()

    def inicializar(self, n):
        for i in range(n):
            valor = random.randint(0, 100)  # Genera un número aleatorio entre 0 y 100
            self.lista.add_Last(valor)

    def ordenar(self):
        # Verificar si la lista está vacía
        if self.lista.is_Empty():
            raise ValueError("La lista está vacía. No se puede ordenar.")

        # Aplicar el algoritmo Bubble Sort
        for i in range(self.lista.size()):
            nodo_actual = self.lista.first()
            nodo_siguiente = nodo_actual.get_Next()

            for j in range(self.lista.size() - 1 - i):
                # Comparar los datos por cédula/ID
                if nodo_actual.get_Data()> nodo_siguiente.get_Data():
                    # Intercambiar los datos
                    temp_data = nodo_actual.get_Data()
                    nodo_actual.set_Data(nodo_siguiente.get_Data())
                    nodo_siguiente.set_Data(temp_data)

                # Avanzar los nodos
                nodo_actual = nodo_siguiente
                nodo_siguiente = nodo_siguiente.get_Next()

    def mostrar(self):
        print(self.lista)
