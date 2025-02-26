from Laboratorio_8.Binerysearchtree import BinarySearchTree
from Laboratorio_8.BSTEntry import BSTEntry


def calcular_clave(identificacion):
    return sum(int(digit) for digit in str(identificacion))

usuarios = [
    ("Juan", 10101013),
    ("Pablo", 10001011),
    ("Maria", 10101015),
    ("Ana", 1010000),
    ("Diana", 10111105),
    ("Mateo", 10110005)
]

bst = BinarySearchTree()


for nombre, id_num in usuarios:
    clave = calcular_clave(id_num)
    bst.insertar(clave, nombre)


print("\nEstructura del Árbol Binario de Búsqueda:")
bst.Mostrar_Arbol()


print("\nValor mínimo en el árbol:", bst.get_min())
print("Valor máximo en el árbol:", bst.get_max())


bst.Recorrido_Inorder()


key_to_search = calcular_clave(10101013)
found_node = bst.Buscar(key_to_search)
if found_node:
    print(f"\nNodo encontrado: ({found_node.key}, {found_node.value})")
else:
    print("\nNodo no encontrado.")


key_to_delete = calcular_clave(1010000)
bst.Eliminar(key_to_delete)
print("\nÁrbol después de eliminar el nodo con clave", key_to_delete)
bst.Mostrar_Arbol()