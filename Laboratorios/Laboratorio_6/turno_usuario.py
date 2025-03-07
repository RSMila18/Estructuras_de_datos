from Laboratorio_6.stack import Stack
from Laboratorio_6.queue import Queue
from Laboratorio_2_y_3.Clases.usuario import Usuario
import os
class TurnoUsuario:
    def __init__(self):
        self.registro = Queue()
        self.usuarioAtendido = Stack()
        self.Usuario = Usuario()
        
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
        current_dir = os.path.dirname(os.path.abspath(__file__))
        full_path = os.path.join(current_dir, "Datos_2", filename)
        with open(full_path, "w", encoding="utf-8") as archivo:
            current = self.registro.data._head
            while current:
                usuario = current.get_Data()
                archivo.write(f"{usuario.get_nombre()}, {usuario.get_id()}\n")
                current = current.get_Next()
                
        full_path = os.path.join(current_dir, "Datos_2", filename2)
        with open(full_path, "w", encoding="utf-8") as archivo:        
            current = self.usuarioAtendido.data._head
            while current:
                usuario = current.get_Data()
                archivo.write(f"{usuario.get_nombre()}, {usuario.get_id()}\n")
                current = current.get_Next()