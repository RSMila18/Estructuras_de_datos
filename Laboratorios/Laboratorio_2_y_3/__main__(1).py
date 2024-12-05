from Clases.direccion import Direccion
from Clases.fecha import Fecha
from Clases.usuario import Usuario

fecha_nacimiento = Fecha("18","10","01")
print(fecha_nacimiento)
mi_dirección = Direccion("Cra 66","111A-29","Boyacá","Medellín","Casa","Primer Piso")
print(mi_dirección)
mi_usuario = Usuario("Maria Camila Rios Mejia", 1193142631, fecha_nacimiento, "Medellín", 3104104958, "mriosm@unal.edu.co", mi_dirección)
print(mi_usuario)