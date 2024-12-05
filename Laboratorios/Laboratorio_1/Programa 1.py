#Programa 1 – Variables, expresiones y estructuras de control
def Max_Min_Sum_Prom(L):
    Max = L[0]
    Min = L[0]
    Sum = 0

    for i in L:
        if i > Max:
            Max = i
        if i < Min:
            Min = i
        Sum += i
    
    promedio = Sum/len(L)

    return f"El valor maximo es: {Max}\nEl valor minimo es: {Min}\nLa suma de los enteros ingresados es: {Sum}\nEl valor promedio es: {promedio}"

n = int(input("Digite la cantidad de números enteros que desea ingresar: "))
L = []
for i in range(n):
    numero=int(input("Ingrese un número: "))
    L.append(numero)

print("\n")
print(Max_Min_Sum_Prom(L))

