from Laboratorio_2_y_3.Clases.usuario import Usuario
from Laboratorio_4.doble_list import DoubleList
from Laboratorio_2_y_3.Clases.fecha import Fecha
from Laboratorio_2_y_3.Clases.direccion import Direccion


usuario_1 = Usuario("Jose Jose Ramirez Torres", 435751178, Fecha("02","04","1969"), "Medellin", 3108025423,"josejose@unal.edu.co", Direccion("Calle 38D", "45-07","La Candelaria", "Medellin", "Los Candelabros", "213"))
usuario_2 = Usuario("Sofia de Jesus Toro", 25899756, Fecha("19","10", "1942"), "Sabanalarga", 3005785624, "sofia42@gmail.com", Direccion("Cra 66", "111A-29", "Boyaca", "Medellín", "Casa", "Segundo Piso"))
usuario_3 = Usuario("Alejandro Zapata Lopez", 1187426598, Fecha("04","12","2002"), "Bogotá", 3115876239, "azapatal@unal.edu.co", Direccion("Calle 42A", "53-52", "Robledo", "Medellín", "Bello Horizonte", "402"))
usuario_4 = Usuario("Angel David Mesa Londoño", 75708115, Fecha("13","03","1983"), "Cali", 3049873610, "admesal@gmail.com", Direccion("Calle 53C", "45-23", "Castilla", "Medellín", "Casa", "Tercer Piso"))
usuario_5 = Usuario("Carla Sanchez Moreno", 1064428009, Fecha("14", "04", "2000"), "Barrancabermeja", 6045826345, "csanchezmo@unal.edu.co", Direccion("Circular Sur 42", "12B-23", "Laureles", "Medellín"))

# Lista doblemente enlazada
coleccion_usuarios = DoubleList()
for usuario in [usuario_1, usuario_2, usuario_3, usuario_4, usuario_5]:
    coleccion_usuarios.add_last(usuario)

# Mostrar usuarios iniciales
print("Usuarios iniciales:")
print(coleccion_usuarios)

# Función para crear un nuevo usuario
def crear_usuario():
    nombre = input("Nombre: ")
    identificacion = int(input("Número de Identificación: "))
    fecha_ = input("Fecha de Nacimiento (dd/mm/aaaa): ")
    dia, mes, anio = fecha_.split('/')
    fecha_nacimiento = Fecha(dia, mes, anio)
    ciudad_nacimiento = input("Ciudad de Nacimiento: ")
    telefono = int(input("Teléfono: "))
    correo = input("Correo Electrónico: ")
    print("Ingrese los datos de su dirección:")
    calle = input("Calle: ")
    nomenclatura = input("Nomenclatura: ")
    barrio = input("Barrio: ")
    ciudad = input("Ciudad: ")
    edificio = input("Edificio: ")
    apto = input("Apartamento: ")
    direccion = Direccion(calle, nomenclatura, barrio, ciudad, edificio, apto)
    return Usuario(nombre, identificacion, fecha_nacimiento, ciudad_nacimiento, telefono, correo, direccion)

# Insertar un usuario al principio
print("\nInsertar un usuario al principio:")
nuevo_usuario_inicio = crear_usuario()
coleccion_usuarios.add_first(nuevo_usuario_inicio)

# Insertar un usuario al final
print("\nInsertar un usuario al final:")
nuevo_usuario_final = crear_usuario()
coleccion_usuarios.add_last(nuevo_usuario_final)

# Mostrar usuarios después de las inserciones
print("\nUsuarios después de insertar al principio y al final:")
print(coleccion_usuarios)
# Insertar un usuario después del tercer nodo
print("\nInsertar un usuario después del tercer nodo:")
nuevo_usuario_intermedio = crear_usuario()
tercer_usuario = coleccion_usuarios.get_node_at(3)  # Obtener el nodo en la posición 3
if tercer_usuario:
    coleccion_usuarios.add_after(tercer_usuario, nuevo_usuario_intermedio)
else:
    print("No hay suficientes nodos para insertar después del tercero.")

# Mostrar usuarios finales
print("\nUsuarios finales después de todas las inserciones:")
print(coleccion_usuarios)