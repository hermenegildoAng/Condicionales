# Realiza un algoritmo que calcule la potencia, para ello pide por teclado 
# la base y el exponente. Pueden ocurrir tres cosas:
# * El exponente sea positivo, sólo tienes que imprimir la potencia.
# * El exponente sea 0, el resultado es 1.
# * El exponente sea negativo, el resultado es 1/potencia con el exponente positivo.

print("Algoritmo que calcule la potencia")

base = int(input("Ingrese el numero a exponenciar: "))
exp = int(input("Ingrese la potencia: "))

t = base ** exp 

print("El resultado es: ",t)