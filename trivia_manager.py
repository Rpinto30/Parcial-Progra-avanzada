print("Aquí ira la clase que administre la trivia")
from data_base import questions_list


class Trivia:
    def __init__(self, game, user):
        counter = 0
        self.user = user
        self.game = game
        self.users_game = {}

class Game:
    def __init__(self, game, score):

class User:
    def __init__(self, user):
        self.users = []

    def add_user(self):
        try:
            user = input("Ingresa el nombre del usuario").lower()
            if user in self.users:
                print("El usuario ya existe dentro del juego.")
            else:
                self.users.append(user)

        except Exception as e:
            print("Error detectado", e)

    def existent_user(self, user):
        user = input("Ingresa el nombre del usuario al que deseas igresar: ").lower()
        if user in self.users:

