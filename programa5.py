# Escribe un programa que pida un nombre de usuario y una contraseña 
# y si se ha introducido "pepe" y "asdasd" se indica "Has entrado al sistema", 
# sino se da un error.

usuario = input("Ingrese el nombre de usuario: ")
password = input("Ingrese la contraseña: ")

if usuario == "pepe" and password == "asdasd":
    print("Has entrado al sistema")
else: 
    print("Error, Usuario y/o contraseña incorrectos")