"""
Hacer una actividad que pida al usuario escribir una cantidad X de nombres de personas (puede hacerlo con el ciclo que considere). Después el sistema deberá demostrar cuales son los nombres que empiezan con la letra "C" sea minúscula o mayúscula.
"""



cant = int(input("Cuantos nombres quiere escribir: \n"))
lista = list()

for i in range(cant):
    nombre = input("Por favor escriba el nombre: \n")
    nombre = nombre.lower()
    lista.append(nombre)

print("Los nombres que comienzan por C son: ")

for i in lista:
    if i[0] == "c":
        
        print(i)


