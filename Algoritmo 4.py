#Elabore una función que lea un carácter y devuelva True si es una vocal, de lo contrario que devuelva 
def funcion(vocal):
    return vocal.lower()in['a','e', 'i','o','u']
vocal = input('Introduce una vocal: ')
if funcion(vocal):
  print('True')
else:
  print('False')

#otra forma
def es_vocal_in_line(vocal):
    return True if vocal in ["a", "e", "i", "o", "u"] else False
#otra forma
def esVocal(vocal):
    vocales = ["a", "e", "i", "o", "u"]

    if vocal in vocales:
        return True
    else:
        return False


vocal = input("Ingrese una vocal: ")
print(esVocal(vocal))