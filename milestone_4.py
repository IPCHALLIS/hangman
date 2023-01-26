import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = []
        self.num_letters = len(word)
        self.num_lives = num_lives
        self.word_list = ["orange", "mango", "peach", "pineapple", "kiwi"]
        self.list_of_guesses = list_of_guesses