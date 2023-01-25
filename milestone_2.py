# %%
import random
# %%
word_list = ["orange", "mango", "peach", "pineapple", "kiwi"]
# %%
word = random.choice(word_list)
# %%
print(word)
# %%
guess = input("Please enter a single letter: ")
# %%
if len(guess) == 1 and guess.isalpha():
    print("Good Guess!")
else:
    print("Oops! That is not a valid input.")
# %%