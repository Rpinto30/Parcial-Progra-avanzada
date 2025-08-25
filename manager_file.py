from os import system as sys
from time import sleep #ESTETICO
from save_data import *
from trivia_manager import *
from presenter import *

def get_points(item): return item[1]
class GameManager:
    def __init__(self):
        self.points_list = {} #Jugador: Puntaje

    def init_game(self):
        user = User()
        user.add_user(self.points_list)
        game = Game()
        game.start_game(self.points_list, user.user_name)
        save_data(self.points_list)


    def show_results(self):
        if self.points_list:
            clear_screen() #ESTETICO
            victory_bot() #ESTETICO
            print_dialog(f"{"":<10}{"NO":10}{"JUGADOR":<20}{"PUNTUACIÓN":>5}",0.02)
            #SORTED(ITERADOR, KEY, REVERSA)
            order_point = dict(sorted(self.points_list.items(), key=get_points, reverse=True))
            for num, (name, point) in enumerate(order_point.items(),1):
                print_dialog(f"{"":<10}{str(num)+")":10}{name.upper():<20}{point:>5}")
            sleep(4.2) #ESTETICO
            clear_screen() #ESTETICO
        else:
            print("No hay jugadores registrados")

    @staticmethod
    def _load_data(self):
        load_data()
        pass

    def delete_name(self, name):
        if name not in self.points_list: raise ValueError(f"No se ha encontrado al jugador: {name}")
        else: del self.points_list[name]
        save_data(self.points_list)

    def delete_all(self):
        self.points_list.clear()
        save_data(self.points_list)
