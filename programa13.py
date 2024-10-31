#################################################################################
#Realiza un programa que pida el dí­a de la semana (del 1 al 7) y escriba 
#el dí­a correspondiente. 
# Si introducimos otro número nos da un error.
#################################################################################

dia = int(input("Ingrese el dia de la semana (1-7): "))

if dia >= 1 and dia <= 7:
    if dia == 1:
        dias = 'Lunes'
    elif dia == 2:
        dias = 'Martes'
    elif dia == 3:
        dias = 'Miercoles'
    elif dia == 4:
        dias = 'Jueves'
    elif dia == 5:
        dias = 'Viernes'
    elif dia == 6:
        dias = 'Sabado'
    elif dia == 7:
        dias = 'Domingo'
    print("El dia ",dia," es: ",dias)
else:
    print("ERROR, NUMERO INCORRECTO")
       