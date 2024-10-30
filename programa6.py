#Programa que lea una cadena por teclado y compruebe si es una letra mayúscula.

print("#Programa que lea una cadena por teclado y compruebe si es una letra mayúscula.")
text = input("Ingrese una letra: ")



if len(text) == 1 and text.isupper():
    print("La cadena es una letra mayúscula.")
else:
    print("La cadena no es una letra mayúscula.")