#La política de cobro de una compañía telefónica es: cuando se realiza una 
#llamada, el cobro es por el tiempo que ésta dura, de tal forma que los primeros 
#cinco minutos cuestan 1 euro, los siguientes tres, 80 céntimos,
#los siguientes dos minutos, 70 céntimos, y a partir del décimo minuto, 50 céntimos.
#Además, se carga un impuesto de 3 % cuando es domingo, y si es otro día, en turno
#de mañana, 15 %, y en turno de tarde, 10 %. 
#Realice un algoritmo para determinar cuánto debe pagar por cada concepto 
#una persona que realiza una llamada.

minutos = int(input("Ingrese la duracion de la llamada en minutos: "))

dia = input("Ingrese e dia de la llamada (1-7): ")

if minutos <= 5 and minutos >= 0:
    costo = 5
    if minutos > 5 and minutos <=8:
        costo = 5 + (minutos-5)*.8
    