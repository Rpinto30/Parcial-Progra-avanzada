from data_base import questions_list
from input_func import *
from questions import Question, MultipleChoiceQuestion, WritingsQuestion
from manager_file import GameManager
import  random
class User:
    def __init__(self):
        self.users = [] # Lista que guarda usuarios

    def add_user(self):
        user = input("Ingresa el nombre del usuario").lower()
        if user in self.users:
                print("El usuario ya existe dentro del juego.")
        else:
                self.users.append(user)

    def show_users(self):
        print("\n Usuarios en el juego:")
        if self.users:
            for user in self.users:
                print(f"- {user}")
        else:
            print("No hay usuarios registrados")

    def delete_user(self, user_deleted):
        user_deleted = input("Ingresa el nombre de usuario que deseas eliminar: ").lower()
        if user_deleted in self.users:
            self.users.remove(user_deleted)
        else:
            print("EL usuario no se encuentra registrado en el juego")

class Game(User):
    def __init__(self):
        super().__init__()
        self.points_list = {}

    def new_game(self, user):
        score = 0
        if user in self.users:
            for user in self.users:
                self.users_game[user] = { user : score}
            print("¡Se ha iniciado un nuevo juego!")
        else:
            print("No se encuentran usuarios registrados.")

    def start_game(self, user):

        user = input("Ingresa el usuario para iniciar el juego: ").lower()
        if user in self.users:
            print("\n Has iniciado el juego!")
            question = random.sample(questions_list, k = 10 )
            for q in range(len(question)):
                print("Pregunta")
                print(question[q].question)
                respuesta = input("Ingresa la respuesta: ").lower()
                if respuesta == question[q].correct_answer.lower():
                    print("La respuesta es correcta")













