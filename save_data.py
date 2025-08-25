import json

def save_data(points:dict):
    with open("data.json", mode="w", encoding="utf-8") as data_file:
        json.dump(points, data_file)


def load_data():
    try:
        with open("data.json", mode="r", encoding="utf-8") as read_file:
            return json.load(read_file)
    except FileNotFoundError: save_data({})
