import random

class Ordenador:

    def __init__(self, capacity):
        self.A = [0] * capacity
        self.limit = capacity

    def inicializar(self):
        self.A = [random.randint(0, 100) for _ in range(self.limit)]  # Genera un número aleatorio entre 0 y 100

    def ordenar_burbuja(self):
        for i in range(self.limit):
            for j in range(1, self.limit - i):
                if self.A[j - 1] > self.A[j]:
                    self.A[j - 1], self.A[j] = self.A[j], self.A[j - 1]

    def ordenar_seleccion(self):
        for i in range(self.limit):
            min_index = i
            for j in range(i + 1, self.limit):
                if self.A[j] < self.A[min_index]:
                    min_index = j
            self.A[i], self.A[min_index] = self.A[min_index], self.A[i]

    def ordenar_insercion(self):
        for i in range(1, self.limit):
            temp = self.A[i]
            j = i
            while j > 0 and self.A[j - 1] > temp:
                self.A[j] = self.A[j - 1]
                j -= 1
            self.A[j] = temp

    def ordenar_mergeSort(self):
        def merge_sort(arr, left, right):
            if left < right:
                mid = (left + right) // 2
                merge_sort(arr, left, mid)
                merge_sort(arr, mid + 1, right)
                merge(arr, left, mid, right)

        def merge(arr, left, mid, right):
            n1 = mid - left + 1
            n2 = right - mid
            
            L = [arr[left + i] for i in range(n1)]
            R = [arr[mid + 1 + j] for j in range(n2)]

            i = j = 0
            k = left
            while i < n1 and j < n2:
                if L[i] <= R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1

            while i < n1:
                arr[k] = L[i]
                i += 1
                k += 1

            while j < n2:
                arr[k] = R[j]
                j += 1
                k += 1

        merge_sort(self.A, 0, self.limit - 1)

    def mostrar(self):
        print(self.A)


    def busqueda_binaria(self, x):
        left, right = 0, self.limit - 1
        while left <= right:
            mid = (left + right) // 2
            if self.A[mid] == x:
                return mid
            elif self.A[mid] < x:
                left = mid + 1
            else:
                right = mid - 1
        return -1
