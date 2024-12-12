from Laboratorio_2_y_3.Clases.usuario import Usuario
from Laboratorio_2_y_3.Clases.direccion import Direccion
from Laboratorio_2_y_3.Clases.fecha import Fecha

class Agenda:

    def __init__(self, limite):
        self.registro = [] * limite
        self.no_reg = 0
        self.capacidad = limite

    def buscar(self, identificacion):
        for user in range(len(self.registro)):
            if self.registro[user].get_id() == identificacion:
                return user
        return -1

    def agregar(self, usuario):
        if self.capacidad == self.no_reg:
            return False
        
        else:
            if self.buscar(usuario.get_id()) != -1:
                return False
        
            else:
                self.registro.append(usuario)
                self.no_reg += 1
                return True
    
    def eliminar(self, identificacion):
        posicion = self.buscar(identificacion)
        if posicion != -1:
            for position in range(posicion, len(self.registro) - 1):
                self.registro[position] = self.registro[position + 1]
            self.registro[-1] = None
            self.no_reg -= 1
            return True
        else:
            return False

        
    def toFile(self, filename='agenda.txt'):
        full_path = "Laboratorios/Laboratorio_2_y_3/Datos/" + filename 
        with open(full_path, "w", encoding="utf-8") as archivo:
            for usuario in self.registro:
                archivo.write(str(usuario) + "\n")
            archivo.close()

    
    def import_Data(self, filename="agenda.txt"):
        ruta = "Laboratorios/Laboratorio_2_y_3/Datos/" + filename
        with open(ruta, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                linea = linea.strip()  # Eliminar saltos de línea o espacios extra
                new_linea = linea.split(",")
                fecha = new_linea[2].split("-")
                new_fecha = Fecha(fecha[0], fecha[1], fecha[2])
                new_direccion = Direccion(new_linea[6], new_linea[7], new_linea[8], new_linea[9], new_linea[10], new_linea[11])
                new_user = Usuario(new_linea[0], int(new_linea[1]), new_fecha, new_linea[3], int(new_linea[4]), new_linea[5], new_direccion)
                self.agregar(new_user)
            archivo.close()


        
        
