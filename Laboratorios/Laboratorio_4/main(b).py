#from Laboratorio_4.doble_list import DoubleList
from Laboratorio_2_y_3.Clases.usuario import Usuario
from Laboratorio_2_y_3.Clases.agenda import Agenda
from Laboratorio_2_y_3.Clases.fecha import Fecha
from Laboratorio_2_y_3.Clases.direccion import Direccion

agenda = Agenda(5)

usuario_1 = Usuario("Jose Jose Ramirez Torres", 435751178, Fecha("02","04","1969"), "Medellin", 3108025423,"josejose@unal.edu.co", Direccion("Calle 38D", "45-07","La Candelaria", "Medellin", "Los Candelabros", "213"))
usuario_2 = Usuario("Sofia de Jesus Toro", 25899756, Fecha("19","10", "1942"), "Sabanalarga", 3005785624, "sofia42@gmail.com", Direccion("Cra 66", "111A-29", "Boyaca", "Medellín", "Casa", "Segundo Piso"))
usuario_3 = Usuario("Alejandro Zapata Lopez", 1187426598, Fecha("04","12","2002"), "Bogotá", 3115876239, "azapatal@unal.edu.co", Direccion("Calle 42A", "53-52", "Robledo", "Medellín", "Bello Horizonte", "402"))
usuario_4 = Usuario("Angel David Mesa Londoño", 75708115, Fecha("13","03","1983"), "Cali", 3049873610, "admesal@gmail.com", Direccion("Calle 53C", "45-23", "Castilla", "Medellín", "Casa", "Tercer Piso"))
usuario_5 = Usuario("Carla Sanchez Moreno", 1064428009, Fecha("14", "04", "2000"), "Barrancabermeja", 6045826345, "csanchezmo@unal.edu.co", Direccion("Circular Sur 42", "12B-23", "Laureles", "Medellín"))

agenda.agregar(usuario_1)
agenda.agregar(usuario_2)
agenda.agregar(usuario_3)
agenda.agregar(usuario_4)
agenda.agregar(usuario_5)

for i in range(2):
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
nuevo_usuario2 = Usuario(nombre, identificacion, fecha_nacimiento_main_2, ciudad_nacimiento, telefono, correo, direccion_main_2)
#def add_first(self, nuevo_Usuario):

#def add_Last(self, nuevo_Usuario2):
