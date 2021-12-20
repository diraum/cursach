class User:
    login = ""
    correct_answers = 0
    def __init__(self, login):
        self.login = login
    def answered_correct(self):
        self.correct_answers += 1

