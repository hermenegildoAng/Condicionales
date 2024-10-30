#Algoritmo que pida tres números y los muestre ordenados (de mayor a menor);

print("#Algoritmo que pida tres números y los muestre ordenados (de mayor a menor);")

n1 = int(input("Ingrese el primer numero: "))
n2 = int(input("Ingrese el segundo numero: "))
n3 = int(input("Ingrese el terrcer numero: "))


if n1 >= n2 and n1 >= n3:
    print(n1)
    if n2 >= n3: 
        print(n2)
        print(n3)
    else:
        print(n3)
        print(n2)
elif n2 >= n1 and n2 >= n3:
    print(n2)
    if n1 >= n3 :
        print(n1)
        print(n3)
    else:
        print(n3)
        print(n1)
elif n3 >= n1 and n3 >= n2:
    print(n3)
    if n1 >= n2:
        print(n1)
        print(n2)
    else:
        print(n2)
        print(n1)
        