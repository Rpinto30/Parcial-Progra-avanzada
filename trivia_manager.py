from data_base import questions_list
from input_func import *
from questions import Question, MultipleChoiceQuestion, WritingsQuestion
from manager_file import GameManager
import  random
class User:
    def __init__(self):
        self.user_name = "" # Lista que guarda usuarios

    def add_user(self, dict_user):
        user = input("Ingresa el nombre del usuario").lower()
        if user in dict_user:
            print(f"Volviendo a jugar como {user}.")
        else:
            print("¡Se ha generado una nueva partida!")
            dict_user[user] = 0 # Nueva partida


    def delete_user(self, user_deleted):
        user_deleted = input("Ingresa el nombre de usuario que deseas eliminar: ").lower()
        if user_deleted in self.users:
            self.users.remove(user_deleted)
        else:
            print("EL usuario no se encuentra registrado en el juego")

class Game(User):
    def __init__(self, usuario):
        super().__init__()
        self.user = user

    def new_game(self, user):
        score = 0
        if user in self.users:
            for user in self.users:
                # self.points_list[user] = { user : score} # Error del point list de diccionario
                pass
            print("¡Se ha iniciado un nuevo juego!")
        else:
            print("No se encuentran usuarios registrados.")

    def start_game(self, point):
        print("\n Has iniciado el juego!")
        question = random.sample(questions_list, k=10)
        for q in question:
            print("Pregunta:")
            answer = q.show_question() # Muestra y Guarda la respuesta
            q.verify_answer(answer, )
            print("La respuesta es correcta")













