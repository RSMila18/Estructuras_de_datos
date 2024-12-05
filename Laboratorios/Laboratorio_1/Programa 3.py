#Programa 3 – Tablas y diccionarios
Usuarios = {"Juan1223":"J12an*.",
            "Maria2345":"M23a*.",
            "Pablo1459":"P14o*.",
            "Ana3456":"A34a*."}
intentos=0
while intentos < 3:
    user = input("Ingrese su nombre de usuario: ")
    password = input("Ingrese su contraseña: ")

    if user in Usuarios and Usuarios[user] == password:
        print("Acceso permitido")
        break
    else:
        intentos+=1
        print("Datos incorrectos")

if intentos == 3:
    print("Lo siento, su acceso no es permitido")