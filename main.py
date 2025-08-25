# Ingreso del menú
from manager_file import  *

load_data()
gm = GameManager()
gm.points_list = load_data()

while True:
    try:
        ado_robot() #ESTETICO
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
                    clear_screen() #ESTETICO
                    mid_bot()
                    salir = input_str("--- ¿Estás seguro que quieres salir?  --- ")

                    match salir:
                        case 'si':
                            clear_screen()  # ESTETICO
                            print("--- Has salido del programa :( ---")
                            crying_bot() #ESTETICO
                            break
                        case 'no':
                            clear_screen() #ESTETICO
                            print("      --- Entonces volvamos a jugar :) --- ")
                            happy_face()
                            sleep(2) #ESTETICO
                            clear_screen() #ESTETICO
                            break
                        case _:
                            clear_screen() #ESTETICO
                            print("      Lo siento... no entiendo lo que me dices")
                            angry_bot() #ESTETICO
                            sleep(2)
                            clear_screen()  #ESTETICO
                if salir == 'si':
                    break
    except KeyboardInterrupt:
        print("\nEEEY! No hagas eso")
        angry_bot() #ESTETICO
        sleep(2) #ESTETICO
    except Exception as e: print("Error!! Hemos encontrado un error...",e)
