#Cadenas
print("\nCadenas")
#Ejercicio1

print("\nEjercicio1")

nombre = input("Diga su nombre")
repetir = float(input("Veces a repetir: "))

print(nombre * int(repetir))


#Ejercicio2

print("\nEjercicio2")

nombre = input("Diga su nombre")

nombre_may = nombre.upper()
nombre_min = nombre.lower()
nombre_modificado = nombre.title()

print(nombre_may)
print(nombre_min)
print(nombre_modificado)


#Ejercicio3

print("\nEjercicio3")

nombre = input("Nombre ")
print(nombre.upper() + " tiene " + str(len(nombre)) + " letras")


#Ejercicio4

print("\nEjercicio4")

tel = input("Introduce un número de teléfono: ")
print('El número de teléfono es ', tel[4:13])


#Ejercicio5

print("\nEjercicio5")


frase = input("Frase: ")
print(frase[::-1])


