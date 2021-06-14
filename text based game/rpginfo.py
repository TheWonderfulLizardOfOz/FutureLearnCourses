class RPGInfo():
    def __init__(self, game_title):
        self.title = game_title

    def welcome(self):
        print("Welcome to " + self.title)

    @staticmethod
    def info():
        print("Made by me.")

    @classmethod
    def credits(cls):
        print("Thanks for playing.")
        print("Created by " + cls.author + ".")
        
