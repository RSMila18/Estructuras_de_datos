class Heap:
    def __init__(self, capacity):
        self.size = 0
        self.capacity = capacity
        self.arr = [None] * capacity
    
    @staticmethod
    def parent(i):
        return (i - 1) // 2
    
    @staticmethod
    def left(i):
        return 2 * i + 1
    
    @staticmethod
    def right(i):
        return 2 * i + 2
    
    def max_heapify(self, i, size):
        l = self.left(i)
        r = self.right(i)

        if l < size and self.arr[l] > self.arr[i]:
            largest = l
        else:
            largest = i

        if r < size and self.arr[r] > self.arr[largest]:
            largest = r

        if largest != i:
            temp = self.arr[i]
            self.arr[i] = self.arr[largest]
            self.arr[largest] = temp
            self.max_heapify(self.arr, largest, size)

    def build_max_heap(self):
        for i in range(self.size // 2 - 1 , -1, -1):
            self.max_heapify(i, self.size)

    def heap_sort(self):
        self.build_max_heap()
        for i in range(self.size - 1, 0, -1):
            temp = self.arr[i]
            self.arr[i] = self.arr[0]
            self.arr[0] = temp
            self.size -= 1
            self.max_heapify(0, self.size)
            
    def insert(self, key):
        if self.size >= self.capacity:
            raise Exception("Capacidad máxima alcanzada.")

        i = self.size
        self.arr[i] = key
        self.size += 1
        
        while i > 0 and self.arr[self.parent(i)] < self.arr[i]:
            
            temp = self.arr[self.parent(i)]
            self.arr[self.parent(i)] = self.arr[i] 
            self.arr[i] = temp
            i = self.parent(i)

    def extract_max(self):
        if self.size <= 0:
            raise Exception("Heap vacío.")
        
        max_ = self.arr[0]
        self.arr[0] = self.arr[self.size - 1]
        self.size -= 1
        self.max_heapify(0, self.size)
        return max_
    
    def heap_maximun(self):
        if self.size <= 0:
            raise Exception("Heap vacío.")
        return self.arr[0]
