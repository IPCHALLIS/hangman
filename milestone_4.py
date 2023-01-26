import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(self.word_list)
        self.word_guessed = ['_']*len(self.word)
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = ["orange", "mango", "peach", "pineapple", "kiwi"]
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in word:
            print(f"Good guess! {guess} is in the word.")
        else:
            print(f"Sorry, {guess} is not in the word. Try again.")

    def ask_for_input(self):
        check_guess(guess)
        while True:
            guess = input("Please enter a single, alphabetical character: ")
            if len(guess) == 1 and guess.isalpha():
                break
            else:
                print("Invalid letter. Please, enter a single alphabetical character.")

hng1 = Hangman(["orange", "mango", "peach", "pineapple", "kiwi"])