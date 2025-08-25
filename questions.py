from os import system as sys #ESTETICO
from time import sleep #ESTETICO
from input_func import *

class Question:
    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer

    def ask_question(self):
        pass

    def show_question(self):
        print(self.question)
        return self.ask_question()

    def verify_answer(self, answer):
        if str(answer).lower() == str(self.correct_answer).lower():
            print("Correcto")
            return True
        else:
            print("Incorrecto")
            return False


class MultipleChoiceQuestion(Question):
    def __init__(self, question, answer, correct_answer):
        super().__init__(question, correct_answer)
        self.answer = answer
    def ask_question(self):
        for num, q in enumerate(self.answer, 1):
            print(f"  {num}) {q}")
        while True:
            ans = input_number("Ingresa el número de tu respuesta: ")-1
            if 0 <= ans <= len(self.answer)-1: return ans
            else: print("\nElige una opción valida\n")


class WritingsQuestion(Question):
    def __init__(self, question, correct_answer):
        super().__init__(question, correct_answer)
    def ask_question(self):
        return input_str("Ingresa tu respuesta: ")
