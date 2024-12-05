from Clases.fecha import Fecha
from Clases.direccion import Direccion
from Clases.usuario import Usuario

nombre = input("Nombre: ")
identificacion = int(input("Numero de Identificacion: "))

#fecha
fecha_ = input("Fecha de Nacimiento(dd/mm/aaaa): ")
fecha_1 = fecha_.split('/')
fecha_nacimiento_main_2 = Fecha(fecha_1[0],fecha_1[1],fecha_1[2])

ciudad_nacimiento = input("Ciudad de Nacimiento: ")
telefono = int(input("Telefono: "))
correo = input("Correo Electronico: ")

#Dirección
calle = input("Ingrese los datos de su direccion.\nCalle: ")
nomenclatura = input("Nomenclatura: ")
barrio = input("Barrio: ")
ciudad = input("Ciudad: ")
edificio = input("Edificio: ")
apto = input("Apto: ")
direccion_main_2 = Direccion(calle,nomenclatura,barrio,ciudad,edificio,apto)

#Nuevo Usuario
nuevo_usuario = Usuario(nombre, identificacion, fecha_nacimiento_main_2, ciudad_nacimiento, telefono, correo, direccion_main_2)
print(nuevo_usuario)