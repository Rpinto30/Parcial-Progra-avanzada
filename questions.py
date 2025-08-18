from input_func import *

class Question:
    def __init__(self, question, answer, correct_answer):
        self.question = question
        self.answer = None

    def ask_question(self):
        pass

    def show_question(self):
        print(self.question)
        return self.ask_question()

    def verify_answer(self):
        pass

class MultipleChoiceQuestion(Question):
    def __init__(self, question, answer, correct_answer):
        super().__init__(question, answer, correct_answer)
    def ask_question(self):
        for num, q in enumerate(self.answer, 1):
            print(f"{num}. {q}")
        return input_number("Ingresa tu respuesta: ")-1

class WritingsQuestion(Question):
    def __init__(self, question, answer, correct_answer):
        super().__init__(question, answer, correct_answer)
    def ask_question(self):
        print(self.question)
        return input_str("Ingresa tu respuesta: ")