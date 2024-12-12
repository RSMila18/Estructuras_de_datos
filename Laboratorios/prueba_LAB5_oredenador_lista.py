from Laboratorio_5.ordenador_lista import OrdenadorLista

if __name__ == "__main__":
    n = 10
    ordenador_lista = OrdenadorLista()

    print("Inicializando la lista:")
    ordenador_lista.inicializar(n)
    ordenador_lista.mostrar()

    print("\nOrdenando la lista:")
    ordenador_lista.ordenar()
    ordenador_lista.mostrar()
