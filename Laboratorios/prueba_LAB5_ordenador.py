from Laboratorio_5.ordenador import Ordenador

if __name__ == "__main__":
    capacidad = 10
    ordenador = Ordenador(capacidad)

    print("Inicializando el arreglo:")
    ordenador.inicializar()
    ordenador.mostrar()

    print("\nOrdenando el arreglo con burbuja:")
    ordenador.ordenar_burbuja()
    ordenador.mostrar()

    print("\nBúsqueda binaria de 50:")
    posicion = ordenador.busqueda_binaria(50)
    print("Encontrado en posición:", posicion if posicion != -1 else "No encontrado")
