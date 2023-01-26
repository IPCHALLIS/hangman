import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        word = random.choice(word_list)
        self.word_guessed = "_"*len(word)
        self.num_letters = len(word)
        self.num_lives = num_lives
        word_list = ["orange", "mango", "peach", "pineapple", "kiwi"]
        self.list_of_guesses = []

