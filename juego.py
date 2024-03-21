from personaje import Personaje
import random

nombre = input("""
¡Bienvenido a Gran Fantasía!

Por favor indique nombre de su personaje: """)

jugador = Personaje(nombre)
orco = Personaje("Orco")

print(jugador.estado)
print(orco.estado)

print("\n¡Oh no!, ¡Ha aparecido un Orco!")

probabilidad_ganar = jugador.mostrar_probabilidad(orco)

mensaje_probabilidad = Personaje.mostrar_dialogo_opcion(probabilidad_ganar)

while mensaje_probabilidad == 1:

    pelea = "G" if random.uniform(0, 1) < probabilidad_ganar else "P"
    if pelea == "G":
        print("""
¡Le has ganado al orco, felicidades!
¡Recibirás 50 puntos de experiencia!
        """)
        jugador.estado = 50
        orco.estado = -30
    else:
        print("""
¡Oh no! ¡El orco te ha ganado!
¡Has perdido 30 puntos de experiencia!
        """)
        jugador.estado = -30
        orco.estado = 50

    print(jugador.estado)
    print(orco.estado)

    probabilidad_ganar = jugador.mostrar_probabilidad(orco)
    mensaje_probabilidad = Personaje.mostrar_dialogo_opcion(probabilidad_ganar)

print("¡Has huido! El orco ha quedado atrás.")

