#Condicionales
print("\nCondicionales")
#Ejercicio1

print("\nEjercicio1")

edad = int(input("Diga su edad "))
if edad < 18:
    print ("Eres menor de edad")
else:
    print("Eres mayor de edad")

#Ejercicio2

print("\nEjercicio2")

contraseña = 1234
password = float(input("Introduce la contraseña: "))
if contraseña == password:
    print("La contaseña coincide")
else:
    print("La contraseña no coincide")


#Ejercicio3

print("\nEjercicio3")

n = float(input("dividendo: "))
m = float(input("divisior: "))
if m == 0:
    print("No se puede dividir por 0")
else:
    print(n/m)

