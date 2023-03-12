palabra = input("Introduzca una palabra:")

def palindromo(palabra):
    for i in range(len(palabra) // 2):
        if palabra[i] != palabra[len(palabra) -1 -i]: # Para que no se cuente el elemento de en medio si la palabra es impar
            return False
    return True

if palindromo(palabra):
    print("Es un palindromo")
else:
    print("No es un palindromo")
