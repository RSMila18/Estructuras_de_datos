from Laboratorio_7.heap import Heap
import random

heap = Heap(5)
heap.arr = [random.randint(0, 100) for i in range(5)]
heap.size = 5
print(heap.arr)

heap.build_max_heap()
print(heap.arr)

heap.heap_sort()
print(heap.arr)

heap.insert(6)
print(heap.arr)