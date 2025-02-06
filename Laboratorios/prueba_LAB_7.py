from Laboratorio_7.heap import Heap
import random

heap = Heap(6)
heap.arr = [random.randint(0, 100) for _ in range(5)] + [None]
heap.size = 5
print( f'Arreglo: {heap.arr}')

heap.heap_sort()
print( f'Arreglo luego de heap_sort(): {heap.arr}')


heap.build_max_heap()
print( f'Arreglo construido con max heap: {heap.arr}')

m = heap.heap_maximun()
print(f'El máximo es: {m}')

heap.insert(8)
print( f'Arreglo luego de insertar un elemento: {heap.arr}')
print('Extrayendo los elementos de mayor a menor:')
while heap.size > 0:
    max_ = heap.extract_max()
    print(max_)

