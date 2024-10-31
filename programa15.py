#################################################################################
# Juego Piedra Papel y Tijera
# Programa que lea las opciones de 2 jugadores, y muestra el resultado
# Empate, gana jugador 1 o gana jugador 2
# Si introducimos una opción que no coindica con piedra, papel o tijera
# Diga que opción Incorrecta
#################################################################################

print("Juego Piedra Papel o Tijeras")

op1 = input("Ingrese la opcion del jugador 1: ")
op2 = input("Ingrese la opcion del jugador 2: ")

op1 = op1.lower()
op2 = op2.lower()

if op1 == 'piedra' or op1 == 'papel' or op1 == 'tijeras' and op2 == 'piedra' or op2 == 'papel' or op2 == 'tijeras':
    if op1 == op2:
        print('EMPATE')
    elif op1 == 'piedra' and op2 == 'tijeras':
        print("Gana el Jugdor 1 ")
    elif op1 == 'piedra' and op2 == 'papel':
        print("Gana Jugador 2")
    elif op1 == 'papel' and op2 == 'tijeras':
        print("Gana el Jugdor 2 ")
    elif op1 == 'papel' and op2 == 'piedra':
        print("Gana Jugador 1")
    elif op1 == 'tijeras' and op2 == 'papel':
        print("Gana el Jugdor 1 ")
    elif op1 == 'tijeras' and op2 == 'piedra':
        print("Gana Jugador 2")

else:
    print("OPCION INCORRECTA")
    