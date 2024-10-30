#El director de una escuela está organizando un viaje de estudios, y requiere 
#determinar cuánto debe cobrar a cada alumno y cuánto debe pagar a la compañía de 
#viajes por el servicio. La forma de cobrar es la siguiente: 
#si son 100 alumnos o más, el costo por cada alumno es de 65 euros; 
#de 50 a 99 alumnos, el costo es de 70 euros, de 30 a 49, de 95 euros, 
#y si son menos de 30, el costo de la renta del autobús es de 4000 euros, 
#sin importar el número de alumnos. 
#Realice un algoritmo que permita determinar el pago a la compañía de autobuses 
#y lo que debe pagar cada alumno por el viaje.

nalum = int(input("Ingrese el total de Alumnos: "))

if nalum >= 100 :
    costo = nalum * 65
    print("El total es: ",costo,' Euros')
elif nalum >= 50 and nalum <= 99 :
    costo = nalum * 70
    print('El costo es: ',nalum,' Euros')
elif nalum > 30 and nalum <= 49 :
    costo = nalum * 95
    print('El costo es: ',costo,' Euros')
else:
    costo = 4000
    print('El costo es: ',costo,' Euros')