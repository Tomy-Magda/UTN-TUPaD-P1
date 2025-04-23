contraseña = input("Introduzca una contraseña entre 8 y 14 caracteres: ")
if len(contraseña) > 14 or len(contraseña) < 8:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
else:
    print("Ha ingresado una contraseña correcta")