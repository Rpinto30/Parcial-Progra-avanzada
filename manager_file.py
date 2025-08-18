from save_data import *

def get_points(item): return item[1]
class GameManager:
    def __init__(self):
        self.points_list = {} #Jugador: Puntaje

    def init_game(self):
        #trivia = Trivia()
        #trivia.start_trivia(self.points_list)
        pass

    def show_results(self):
        #SORTED(ITERADOR, KEY, REVERSA)
        order_point = dict(sorted(self.points_list.items(), key=get_points, reverse=True))
        for num, (name, point) in enumerate(order_point.items(),1):
            print(f"{"":<10}{str(num)+")":10}{name.upper():<20}{point:>5}")

    @staticmethod
    def load_datas(self): #ES ESTATICA, POR ESO EL DECORADOR
        load_data()

    def delete_name(self, name):
        if name not in self.points_list: raise ValueError(f"No se ha encontrado al jugador: {name}")
        else: del self.points_list[name]
        save_data(self.points_list)

    def delete_all(self):
        self.points_list.clear()
        save_data(self.points_list)