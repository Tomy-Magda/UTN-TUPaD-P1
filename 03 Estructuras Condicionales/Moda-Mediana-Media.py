from statistics import mean, mode, median
import random 

numeros_aleatorios = [random.randint(1, 100) for i in range (10)]
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)
print("Los números aleatorios son :", numeros_aleatorios)
print("La media de los números son: ", media)
print("La mediana de los números es: ",mediana)
print("La moda de los números es: ", moda)
if media > mediana and mediana > moda:
    print("El sesgo es positivo")
elif media < mediana and mediana < moda:
    print("El sesgo es negativo")
elif media == mediana and mediana == moda:
    print("No hay sesgo")