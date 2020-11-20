"""
Realice una FUNCIÓN en Python que calcule el índice de masa corporal de una persona y diga el estado en que se encuentre. Debe recibir los parámetros necesarios.
"""
print("Para calcular el Indice de masa corporal siga las indicaciones: ")

peso = float(input("Por favor indique su peso: \n"))
altura = float(input("Por favor indique su Altura en metros: ejemplo 1.80: \n"))**2

def calculo_indice(peso, altura):

    indice = round(peso/altura, 2)

    print("Su indice de masa corporal es: " + str(indice))

    if indice < 18.5:
        print("Ud tiene peso insuficiente")
    if indice >= 18.5 and indice <= 24.9:
        print("Ud tiene un peso normal")
    if indice >= 25 and indice <= 26.9:
        print("Ud tiene Sobrepeso grado I")
    if indice >= 27 and indice <= 29.9:
        print("Ud tiene Sobrepeso grado II (preobesidad)")
    if indice >= 30 and indice <= 34.9:
        print("Ud tiene Obesidad de tipo I")
    if indice >= 35 and indice <= 39.9:
        print("Ud tiene Obesidad de tipo II")
    if indice >= 40 and indice <= 49.9:
        print("Ud tiene Obesidad de tipo III (mórbida)")
    if indice > 50:
        print("Ud tiene Obesidad de tipo IV (extrema)")


calculo_indice(peso, altura)