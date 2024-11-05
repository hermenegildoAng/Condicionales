#################################################################################
#Realiza un programa que pida por teclado el resultado (dato entero) obtenido 
#al lanzar un dado de seis caras y muestre por pantalla el número en letras 
#(dato cadena) de la cara opuesta al resultado obtenido.
#* Nota 1: En las caras opuestas de un dado de seis caras están los números: 
#1-6, 2-5 y 3-4.
#* Nota 2: Si el número del dado introducido es menor que 1 o mayor que 6, 
#se mostrará el mensaje: "ERROR: número incorrecto.".
#################################################################################

cara = int(input("Ingrese el resultado del dado:  "))


if cara >= 1 and cara <= 6:
    if cara == 1:
        cap = 'seis'
    elif cara == 2:
        cap = 'cinco'
    elif cara == 3:
        cap = ' cuatro'
    elif cara == 4:
        cap = 'tres'
    elif cara == 5:
        cap = 'dos'
    elif cara == 6:
        cap = 'uno'
    
    print('La cara opuesta es: ', cap)    
    
        
else:
    print('ERROR, NUMERO INCORRECTO ')
    
