'''
    condicionales if: 
        Evaluan expresiones booleanas
    
    estructura: 
        if expresion:
            instrucciones
            
        if expresion:
            instrucciones
        else: 
            instrucciones
            
        if expresion:
            instrucciones
        elif expresion:
            instrucciones
        else:
            instrucciones
'''

print("Programa que verifica que si un numero es positivo")

n = int(input("Ingrese un numero: "))

if n > 0:
    print("El numero es positivo")
else: 
    print("El numero es negativo")
        
        
print("Fin del programa ")

print("Programa que verifica que si un numero es par")

nu = int(input("Ingrese un numero: "))

if nu % 2 == 0:
    print("El numero es par")
else: 
    print("El numero es impar")
        
        
print("Fin del programa ")