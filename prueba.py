import datetime

# Obtener el año actual
year_now = datetime.datetime.now().year

# Pedir datos al usuario
nombre = input("¿Cómo te llamas? ")
edad = int(input("¿Cuántos años tienes? "))

# Calcular año en que cumplirá 100
ano_100 = year_now + (100 - edad)

print(f"\nHola, {nombre}. Cumplirás 100 años en el año {ano_100}.\n")

# Pequeño menú de acciones
print("¿Qué quieres hacer ahora?")
print("1. Repetir el mensaje")
print("2. Salir")

opcion = input("Elige una opción (1/2): ")

if opcion == "1":
    veces = int(input("¿Cuántas veces quieres repetirlo? "))
    for _ in range(veces):
        print(f"{nombre}, cumplirás 100 años en {ano_100}.")
else:
    print("¡Adiós!")
