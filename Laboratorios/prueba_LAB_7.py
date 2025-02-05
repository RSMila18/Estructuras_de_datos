from Laboratorio_7.heap import Heap
import random

heap = Heap(6)
heap.arr = [random.randint(0, 100) for _ in range(5)] + [None]
heap.size = 5
print(heap.arr)

heap.build_max_heap()
print(heap.arr)

heap.insert(8)
print(heap.arr)

heap.heap_sort()
print(heap.arr)
