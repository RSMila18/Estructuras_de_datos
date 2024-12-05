#Programa 2 – Archivos y cadenas
with open("Laboratorios/Laboratorio_1/test_pr2.txt", "r", encoding="utf-8") as file:
    archivo = file.read()
contador = archivo.lower().split().count("no")
print(f"La palabra 'en' se repite {contador} veces")