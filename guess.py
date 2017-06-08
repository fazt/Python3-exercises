# Este es el juego de adivina el numero
# tiene que cumplir con los siguientes requerimientos:
    # tiene que saludar y preguntar al nombre del usuario
    # preguntar al usuario un numero que esta entre un intervalo
    #

# en este ejercicio practicars:
    # importar modulos
    # bucle while
    #

import random

guessesTaken = 0

print("¡Hola! ¿Cual es tu Nombre?")
username = input()

number = random.randint(1, 20)
print('Bueno,', username, 'Estoy pensando un numero entre 1 y 20.')

while guessesTaken < 6:
    print("Adivina un Numero Entero: ")
    guess = input()
    guess = int(guess)

    guessesTaken = guessesTaken + 1

    if guess < number:
        print("Tu numero es demasiado Bajo")
    elif guess > number:
        print("Tu numero es demasiado alto")
    else:
        break

if guess == number:
    guessesTaken = str(guessesTaken)
    print("Buen Trabajo", username, "Has adivinado el numero en", guessesTaken, "intentos.")
else:
    number = str(number)
    print("No, el numero que tenia pensado era ", number)
