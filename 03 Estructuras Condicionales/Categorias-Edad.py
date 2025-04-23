edad = int(input("Ingrese su edad: "))
if edad < 12:
    print("Usted pertenece a la categorias de niños")
elif edad >= 12 and edad < 18:
    print("Usted pertenece a la categoria de adolecentes")
elif edad >= 18 and edad < 30:
    print("Usted pertenece a la categoria de adulto joven")
elif edad >= 30:
    print("Usted pertenece a la categoria de adulto")