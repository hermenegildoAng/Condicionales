"""
Ejercicio 11:
    La política de cobro de una compañía telefónica es: cuando se realiza una 
    llamada, el cobro es por el tiempo que ésta dura, de tal forma que los primeros 
    cinco minutos cuestan 1 euro, los siguientes tres, 80 céntimos,
    los siguientes dos minutos, 70 céntimos, y a partir del décimo minuto, 50 céntimos.
    Además, se carga un impuesto de 3 % cuando es domingo, y si es otro día, en turno
    de mañana, 15 %, y en turno de tarde, 10 %. 
    Realice un programa para determinar cuánto debe pagar por cada concepto 
    una persona que realiza una llamada.
"""
duracion = int (input("Ingresa la duración de la llamada en minutos: "))
dia = input("Ingresa el día de la llamada: ")
turno = ""
if dia != "domingo":
    turno = input ("Ingresa el turno de la llamada (mañana/tarde: ")
if duracion <= 5:
    costo = (duracion * 1)
elif duracion <= 8:
    costo = (5 * 1) + (duracion - 5) * 0.8
elif duracion <= 10:
    costo = (5 * 1) + (3 * 0.8) + (duracion - 8) * 0.7
else:
    costo = (5 * 1) + (3 * 0.8) + (2 * 0.7) + (duracion - 10) * 0.5
if dia == "domingo":
    impuesto = (costo * 0.03)
else:
    if turno == "mañana":
        impuesto = (costo * 0.15)
    elif turno == "tarde":
        impuesto = (costo * 0.10)
costo_total = costo + impuesto
print(f"El costo de la llamada es {costo_total} euros")