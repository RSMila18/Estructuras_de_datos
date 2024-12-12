from Laboratorio_4.lista_simple import List

def remove(L,x):
    temp = L.first()
    anterior = None
    while temp is not None:
        if temp.get_Data() == x:
            if temp == L.first():
                L.remove_First()
            elif temp == L.last():
                L.remove_Last()
            else: #intermedio
                anterior.set_Next(temp.get_Next())
                temp.set_Next(None)
                L.set_Size(L.size()-1)
            return L
        else:
            anterior = temp
            temp = temp.get_Next()
    return f"No existe el valor {x} en esta lista: {L}"
        
Almacen = List()
Almacen.add_First(2)
for i in range(4,22,2):
    Almacen.add_Last(i)
print(Almacen)
print(remove(Almacen,1))
print(remove(Almacen,10))
print(remove(Almacen,20))