from data_base import questions_list
from input_func import *
import  random

class User:
    def __init__(self):
        self.user_name = input_str("Ingresa el nombre del usuario").lower() # String

    def add_user(self, dict_user):
        if self.user_name in dict_user:
            print(f"Volviendo a jugar como {self.user_name}.")
        else:
            print("¡Se ha generado una nueva partida!")
            dict_user[self.user_name] = 0 # Nueva partida

    def delete_user(self, dict_user):
        user_deleted = input_str("Ingresa el nombre de usuario que deseas eliminar: ").lower()
        if user_deleted in dict_user:
            del dict_user[user_deleted]
        else:
            print("EL usuario no se encuentra registrado en el juego")

class Game(User):
    def __init__(self):
        super().__init__()
    def start_game(self, point, username):
        print("\n Has iniciado el juego!")
        question = random.sample(questions_list, k=10)
        for q in question:
            print("Pregunta:")
            answer = q.show_question() # Muestra y Guarda la respuesta
            q.verify_answer(answer, point[username])
            print("La respuesta es correcta")













