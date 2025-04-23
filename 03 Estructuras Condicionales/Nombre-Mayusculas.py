nombre = str(input("Ingrese su nombre: "))
numero = int(input("Ingrese el número de la opción que desee (1: Nombre en mayúsculas, 2: Nombre en minúsculas, 3: Nombre con primera letra en mayúscula): "))
if numero == 1:
    print(nombre.upper())
elif numero == 2:
    print(nombre.lower())
elif numero == 3:
    print(nombre.title())
else:
    print("Opción invalida, ingrese un número entre 1, 2 y 3")