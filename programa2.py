# Programa que pida un número y diga si es positivo, negativo o 0.

print("# Programa que pida un número y diga si es positivo, negativo o 0.")
n = int(input("Escriba un numero: "))

if n < 0: 
    print("El numero es negativo")
elif n > 0:
    print("El numero es positivo")
else: 
    print("El numero es 0")