"""
Pide números y mételos en una lista, cuando el usuario meta un 0 ya dejaremos de insertar. Por último, muestra los números ordenados de menor a mayor.
"""

numero = int(input("Por favor ingresar un número: \n"))
lista_num =list()

while numero != 0:
    
    lista_num.append(numero)
    numero = int(input("Por favor ingresar un número: \n"))

lista_num = sorted(lista_num)

print(lista_num)
