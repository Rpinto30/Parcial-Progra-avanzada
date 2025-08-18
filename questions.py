
class Question:
    def __init__(self):
        self.question = str
        self.answer = None

    def ask_question(self):
        pass

    def show_question(self):
        print(self.question)
        return self.ask_question()



