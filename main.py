print("AQUÍ VA EL MENÚ DONDE EL USUARIO INTERACTUARÁ")

# Ingreso del menú

from presenter import ado_robot, error_bot

while True:
    ado_robot()
    print("\n --- ¡Bienvenido al juego de Trivia! ---")
    print("1. Ingresar al juego")
    print("2. Visualizar puntajes y eliminar usuario")
    print("3. Salir")

    option1 = int(input("Ingresa la opcion de tu preferencia (1 - 2): "))
    # Inicio de match (ejecucion de opciones)
    match option1:
        case 1:
            print("\n --- Frase de juego ---")
            print("1. Jugar de nuevo")
        case 4: break


