"""
Escribir una función que cuente la cantidad de apariciones de cada carácter en una cadena de texto, y los devuelva en un diccionario.
"""

texto = input("\nDigite un texto: \n\n")


def apariciones(cadena):
    cadena = cadena.replace(",","")
    cadena = cadena.replace(" ", "")
    cadena = cadena.replace(".", "")
    cadena = cadena.lower()
    
    dic_letras = dict()

    for i in cadena:
        dic_letras[i] = dic_letras.get(i,0) + 1

    for key, value in dic_letras.items():
          print(key + ": "+ str(value))

print("\nCada carácter se repite: \n")

apariciones(texto)
