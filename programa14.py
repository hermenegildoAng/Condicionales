#################################################################################
#Escribe un programa que pida un número entero entre uno y doce e imprima el 
#número de días que tiene el mes correspondiente.
# Si introducimos otro número nos da un error.
#################################################################################

mes = int(input('Ingrese el mes (1-12): '))

if mes >= 1 and mes <= 12:
    if mes == 1:
        mess = 31
    elif mes == 2:
        mess = 29
    elif mes == 3:
        mess = 31
    elif mes == 4:
        mess = 30
    elif mes == 5:
        mess = 31
    elif mes == 6:
        mess = 30
    elif mes == 7:
        mess = 31
    elif mes == 8:
        mess = 31
    elif mes == 9:
        mess = 30
    elif mes == 10:
        mess = 31
    elif mes == 11:
        mess = 30
    elif mes == 12:
        mess = 31
    print("El mes ",mes," tiene: ",mess," dias")
else:
    print("ERROR, NUMERO INCORRECTO")
       