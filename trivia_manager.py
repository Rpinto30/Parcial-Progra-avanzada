from data_base import questions_list
from input_func import *


class Trivia:
    def __init__(self):
        self.users_game = {}

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





