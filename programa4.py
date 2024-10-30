# Crea un programa que pida al usuario dos números y muestre su división 
# si el segundo no es cero, o un mensaje de aviso en caso contrario.

n1 = int(input("Ingresa el primer numero: "))
n2 = int(input("Ingresa el segundo numero: "))

if n2 != 0: 
    r = n1 / n2
    print("El resultado es: ",r)
else:
    print("ERROR, no se puede dividir entre 0")