from Laboratorio_6.stack import Stack
from Laboratorio_6.queue import Queue
from Laboratorios.Laboratorio_2_y_3.Clases.usuario import Usuario

class TurnoUsuario:
    def __init__(self):
        self.registro = Queue()
        self.usuarioAtendido = Stack()
        
    def registrar(self, Usuario):
        self.registro.enqueue(Usuario)
        
    def atenderSiguiente(self):
        if self.registro.isEmpty():
            "No hay usuarios por atender"
            return None
        else:
            usuario_atendido = self.registro.dequeue()
            self.usuarioAtendido.push(usuario_atendido)
            return "El usuario ha sido atendido"
        
    def toFile(self, filename='usuariospendientes.txt', filename2='usuariosatendidos.txt'):
        full_path = "Laboratorios/Laboratorio_2_y_3/Datos/" + filename 
        with open(full_path, "w", encoding="utf-8") as archivo:
            current = self.registro.data._head
            while current:
                usuario = current.get_Data()
                archivo.write(f"{usuario.get_nombre()}, {usuario.get_id()}\n")
                current = current.get_Next()
                
        full_path = "Laboratorios/Laboratorio_2_y_3/Datos/" + filename2 
        with open(full_path, "w", encoding="utf-8") as archivo:        
            current = self.usuarioAtendido.data._head
            while current:
                usuario = current.get_Data()
                archivo.write(f"{usuario.get_nombre()}, {usuario.get_id()}\n")
                current = current.get_Next()