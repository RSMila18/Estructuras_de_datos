from Laboratorio_4.doble_list import DoubleList
from Laboratorio_2_y_3.Clases.usuario import Usuario
class OrdenadorAgenda:
    def __init__(self):
        self.L = DoubleList()
        
    def agregarUsuario(self, usuario):
        new_usuario = Usuario(usuario)
        self.L.add_last(new_usuario)

    def ordenar(self):
        #Ordena la lista de usuarios según la cédula (menor a mayor) usando burbuja.
        if self.Lis_Empty() == True:
            raise ValueError("La lista está vacía. No se puede ordenar.")

        current = self.L.first()
        while current is not None:
            next_node = current.next
            while next_node is not None:
                if current.data.get_id() > next_node.data.get_id():
                    temp = current.data
                    current.data = next_node.data
                    next_node.data = temp
                next_node = next_node.next
            current = current.next

    def mostrar(self):
        current = self.L.first()
        while current is not None:
            print(current.data)  # Llama al método __str__() de Usuario para imprimir la info
            current = current.next
