from data_base import questions_list
from input_func import *
import random
from presenter import *


class User:
    def __init__(self):
        clear_screen()
        happy_face()
        self.user_name = input_str("Ingresa tú nombre de jugador: ") # String

    def add_user(self, dict_user):
        if self.user_name in dict_user:
            print(f"Volviendo a jugar como {self.user_name}.")
        else:
            print(f"¡Se ha generado una nueva partida como {self.user_name}!")
            dict_user[self.user_name] = 0 # Nueva partida

class Game:
    def __init__(self):
        super().__init__()
    def start_game(self, point, username):
        sesion_points = 0 #Para contar los puntos unicamente de este juego
        clear_screen() #ESTETICO
        print_dialog("         ---Listo???---",0.1)
        sleep(1.2)
        question = random.sample(questions_list, k=10) #ELIGE ALEATOREMENTE 10 PREGUNTAS SIN REPETIR Y GUARDA EN LISTA
        #AQUÍ COMIENZA LA TRIVIA
        for num,q in enumerate(question,1):
            mid_bot()  # ESTETICO
            print(f"\nPregunta {num}:")
            answer = q.show_question() # Muestra y Guarda la respuesta
            if q.verify_answer(answer):
                point[username]+=1
                sesion_points += 1
            sleep(2) #ESTETICO
            clear_screen() #ESTETICO

        #SE IMPRIME MENSAJE FINAL
        clear_screen() #ESTETICO
        print_dialog(str("Tu resultado de este juego fue de...").strip())
        sleep(0.8) #ESTETICO
        print(f"{sesion_points} puntos!") #TOD ESTO ES ESTETICO
        sleep(1.5) #ESTETICO
        if 0 <= sesion_points <=5:
            crying_bot()
            print("        Mejor suerte la proxima...      ")
        elif 6 <= sesion_points <= 9:
            happy_face()
            print("        MUY BIEN JUGADO!!!      ")
        else:
            victory_bot()
            print("      EXCELENTE!! JUEGO PERFECTO!!!      ")
        print_dialog(f"\n      Se agregan a tu puntaje anterior... Tienes {point[username]} en total!")
        sleep(3)