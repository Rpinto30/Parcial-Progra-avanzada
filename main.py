# Ingreso del menú
from presenter import *
from manager_file import  *

load_data()
gm = GameManager()
gm.points_list = load_data()

while True:
    ado_robot()
    print("\n --- ¡Bienvenido al juego de Trivia! ---")
    print("1. Ingresar al juego")
    print("2. Visualizar puntajes ")
    print("3. Salir")

    option1 = input_number("Ingresa la opcion de tu preferencia (1 - 3): ")

    # Inicio de match (ejecucion de opciones)
    match option1:
        case 1:
            print("\n --- ¿Listo para jugar?  ---")
            gm.init_game()
        case 2:
            gm.show_results()
        case 3:
            while True:
                salir = input_str("--- ¿Estás seguro que quieres salir?  --- ")
                mid_bot()
                match salir:
                    case 'si':
                        print("--- Has salido del programa :( ---")
                        crying_bot()
                        break
                    case 'no':
                        print(" --- Entonces volvamos a jugar :) --- ")

                    case _:
                        print("Has ingresado un dato erroneo.")
            if salir == 'si':
                break