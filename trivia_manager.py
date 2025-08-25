from data_base import questions_list
from input_func import *
import  random

class User:
    def __init__(self):
        self.user_name = input_str("Ingresa el nombre del usuario: ").lower() # String

    def add_user(self, dict_user):
        if self.user_name in dict_user:
            print(f"Volviendo a jugar como {self.user_name}.")
        else:
            print("¡Se ha generado una nueva partida!")
            dict_user[self.user_name] = 0 # Nueva partida

class Game:
    def __init__(self):
        super().__init__()
    def start_game(self, point, username):
        print("\n Has iniciado el juego!")
        question = random.sample(questions_list, k=10)
        for num,q in enumerate(question,1):
            print(f"\nPregunta {num}:")
            answer = q.show_question() # Muestra y Guarda la respuesta
            if q.verify_answer(answer): point[username]+=1














