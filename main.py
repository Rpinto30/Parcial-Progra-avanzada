print("AQUÍ VA EL MENÚ DONDE EL USUARIO INTERACTUARÁ")

# Ingreso del menú

from presenter import ado_robot, error_bot
from trivia_manager import Trivia, User

t = Trivia()
u = User()

while True:
    ado_robot()
    print("\n --- ¡Bienvenido al juego de Trivia! ---")
    print("1. Ingresar al juego")
    print("2. Visualizar puntajes ")
    print("3. Eliminar usuario")
    print("3. Salir")

    option1 = int(input("Ingresa la opcion de tu preferencia (1 - 2): "))
    # Inicio de match (ejecucion de opciones)
    match option1:
        case 1:
            print("\n --- ¿Listo para jugar?  ---")
            print("1. Jugar de nuevo")
            print("2. Nueva partida")


            option2 = input("Ingresa la opción de tu preferencia: ")
            match option2:
                case 1:
                    print("\n --- Juego de trivia --- ")
                    print("1. Jugar en partida existente ")
                    print("2. Crear una nueva partida")
                case 2:

                    break
        case 4: break


