import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.num_lives = num_lives
        self.word_list = word_list
        self.word = random.choice(word_list)
        self.word_guessed = ['_']*len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")

    def ask_for_input(self):
        while True:
            guess = input("Please enter a single, alphabetical character: ")
            if len(guess) != 1 and guess != guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif self.word_guessed(guess) in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                break


word_list = ["orange", "mango", "peach", "pineapple", "kiwi"]
hng1 = Hangman(word_list)