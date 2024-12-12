from Laboratorio_4.doble_list import DoubleList
from Laboratorio_2_y_3.Clases.usuario import Usuario
from Laboratorio_2_y_3.Clases.direccion import Direccion
from Laboratorio_2_y_3.Clases.fecha import Fecha

class OrdenadorAgenda:

    def __init__(self):
        self.L = DoubleList()
        
    def agregarUsuario(self, usuario):
        #Angel David Mesa Londoño,75708115,13-03-1983,Cali,3049873610,admesal@gmail.com,Calle 53C,45-23,Castilla,Medellín,Casa,Tercer Piso
        new_linea = str(usuario).split(",")
        fecha = new_linea[2].split("-")
        new_fecha = Fecha(fecha[0], fecha[1], fecha[2])
        new_direccion = Direccion(new_linea[6], new_linea[7], new_linea[8], new_linea[9], new_linea[10], new_linea[11])
        new_user = Usuario(new_linea[0], int(new_linea[1]), new_fecha, new_linea[3], int(new_linea[4]), new_linea[5], new_direccion)
        self.L.add_last(new_user)

    def ordenar(self):
        if self.L.is_Empty():
            raise ValueError("La lista está vacía. No se puede ordenar.")
        n = self.L.size()
        # Aplicar el algoritmo Bubble Sort
        for i in range(n):
            nodo_actual = self.L.first()
            nodo_siguiente = nodo_actual.get_Next()
            for j in range(n - 1 - i):
                # Comparar los datos (en este caso, por cédula/ID)
                if nodo_actual.get_Data().get_id() > nodo_siguiente.get_Data().get_id():
                    # Intercambiar los datos de los nodos
                    temp_data = nodo_actual.get_Data()
                    nodo_actual.set_Data(nodo_siguiente.get_Data())
                    nodo_siguiente.set_Data(temp_data)
                nodo_actual = nodo_siguiente
                nodo_siguiente = nodo_siguiente.get_Next()

    def mostrar(self):
        print(self.L)

