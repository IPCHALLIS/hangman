# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it.

## Milestone 2
In milestone_2.py I imported the random module with the choice method. This was used to randomly select a word from the word_list variable. Following this, I created a new variable called guess and assigned this to a user input function. From here, I implemented if-else statements to check if the user had entered a single alphabetical letter. This printed a different message in the termianl depending on whether the input was valid or invalid.

To start working on this project within VSCode I initially had to clone and copy the HTTPS repository link. I then pasted this into the terminal window, preceded by the "git clone" command. I created the milestone_2.py file from the Bash terminal using the "touch" command. Since then, I have been using the "Commit" and "Sync" options that are available in VSCode's 'Source Control' menu as this seems to make communication with GitHub much faster than the terminal commands.

## Milestone 4
In milestone_4.py I focus on implementing the code I had written in milestones 2 and 3. The main purpose of Milestone 4 is to construct a class called Hangman which involves importing the random module seen in milestone 2. Afterwards, I define the 'init' function and pass three parameters: 'self', 'word_list' and set 'num_lives = 5'. Then, I define the attributes of the class for usage in my two methods later. These methods mimick the functions created in milestone 3. However, I modify them to some degree in order to accomodate the attributes I define previously.

The first method (check_guess) takes 'self' and 'guess' as parameters. It converts the user's guess to lowercase and checks if the user's chosen letter is in the mystery word. If correct, it returns a print statement and replaces '_' in the word_guessed attribute for the correct letter, and reduces the num_letters attribute by 1. If the guess is incorrect, it reduces the num_lives attribute by 1 and returns two print statements. Finally, outside of both (correct/incorrect) conditions I call the list_of_guesses attribute and append the user's guess to the list.

The second method (ask_for_input) takes only 'self' as a parameter. Here I create a while-loop and set it to 'True'. Inside the loop I assign guess to input(). This way the loop keeps running for the duration of the game (win or lose). The loop also contains one if-block that checks whether the guess is a single letter, and alphabetical. If not, it returns a print statement: 'invalid input..'. There is also an elif-block for checking whether the user repeats an entered letter. This searches the list_of_guesses attribute from the first method. If this condition is met, it returns a print statement, reminding the user not to use the same guess again. Lastly, I create an else-block in case the previous conditions are not met. In this scenario, I call the check_guess method and use 'break' to falsify the while-loop, and move outside.

## Milestone 5
In the final stage of my Hangman project I create a method called 'play_game' which takes one parameter: word_list. I define this outside the scope of the Hangman class in order to inherit its methods and attributes. I initially struggled with trying to call the object/instance I wanted to use for the 'play_game' method. However, I realised that I needed to add the name of the object as a prefix to the methods and attributes I was calling. For example, I faced multiple errors saying "ask_for_input" is not defined. This was because I did not specify 'game.ask_for_input'. The 'game' object was assigned to 'Hangman()'. Had I realised what this meant at first, it would have run as intended.

The next issue I noticed was that I had not printed 'self.word_guessed', at the end of my 'init' function. Hence, the user would not have seen the empty spaces they needed to replace with their own guesses. I remedied this issue and run the file again to test its functionality and it worked as expected. Lastly, I added another print statement for 'self.word_guessed' inside the 'check_guess' method. I placed it underneath the if-block so that it would print an updated version of itself so the user can track their correct guesses. However, I also made sure I was outside the for-loop to prevent multiple print statements simultaneously.

Overall, I found the game to work fairly smoothly. Nevertheless, I think there is definitely room for tidying and improving the user's experience when they interact with the terminal.

## Areas for Improvement

1. Print statements could be spaced out more to allow for greater readability.

2. To enhance the visual aesthetic of the game, a hangman image could be displayed in the terminal window with a stage by stage development that reflects the state of the game.

3. To facilitate greater replayability; replace the word_list with a random word generator that searches a vocabulary database using API calls.