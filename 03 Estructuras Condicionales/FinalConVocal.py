palabra_frase = input("Ingrese una palabra o frase: ")
if palabra_frase[-1] in "aeiou":
    print(f"{palabra_frase}!")
else:
    print(palabra_frase)