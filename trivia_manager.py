from data_base import questions_list
from input_func import *
import  random

class User:
    def __init__(self):
        self.user_name = "" # Lista que guarda usuarios

    def add_user(self, dict_user):
        user = input_str("Ingresa el nombre del usuario").lower()
        if user in dict_user:
            print(f"Volviendo a jugar como {user}.")
        else:
            print("¡Se ha generado una nueva partida!")
            self.user_name = user
            dict_user[user] = 0 # Nueva partida


    def delete_user(self, dict_user):
        user_deleted = input_str("Ingresa el nombre de usuario que deseas eliminar: ").lower()
        if user_deleted in dict_user:
            del dict_user[user_deleted]
        else:
            print("EL usuario no se encuentra registrado en el juego")

class Game(User):
    def __init__(self, user):
        super().__init__()
        self.user = user

    def start_game(self, point):
        print("\n Has iniciado el juego!")
        question = random.sample(questions_list, k=10)
        for q in question:
            print("Pregunta:")
            answer = q.show_question() # Muestra y Guarda la respuesta
            q.verify_answer(answer, )
            print("La respuesta es correcta")













