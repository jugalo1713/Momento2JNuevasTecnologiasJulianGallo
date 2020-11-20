"""
Escribir una función que reciba una cadena y devuelva un diccionario con la cantidad de apariciones de cada palabra en la cadena. Por ejemplo, si recibe "Qué lindo día que hace hoy" debe devolver: 'que': 2, 'lindo': 1, 'día': 1, 'hace': 1, 'hoy': 1
"""

texto = input("Digite un texto: \n")


def apariciones(cadena):
    cadena = cadena.replace(",","")
    cadena = cadena.replace(".", "")
    cadena = cadena.lower()
    lista_palabras = cadena.split()
    dic_palabras = dict()

    for i in lista_palabras:
        dic_palabras[i] = dic_palabras.get(i,0) + 1
  
    for key, value in dic_palabras.items():
        print(key + ": "+ str(value))

apariciones(texto)

