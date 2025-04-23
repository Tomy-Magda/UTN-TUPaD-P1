magnitud_terremoto = int(input("Ingrese la magnitud de terremoto: "))
if magnitud_terremoto < 3:
    print("Muy leve (imperceptible)")
elif magnitud_terremoto >= 3 and magnitud_terremoto < 4:
    print("Leve (ligeramente perceptible)")
elif magnitud_terremoto >= 4 and magnitud_terremoto < 5: 
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud_terremoto >= 5 and magnitud_terremoto < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif magnitud_terremoto >= 6 and magnitud_terremoto < 7: 
    print("Muy fuerte (puede causar daños significativos)")
elif magnitud_terremoto >= 7:
    print("Extremo (puede causar graves daños a gran escala)")


