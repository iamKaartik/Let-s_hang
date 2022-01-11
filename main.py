#todo - 1 Randomly choose a word from the list and assign it to a variable called chosen_word.
import random
import hangman_words
from hangman_art import stages,logo

chosen_word = random.choice(hangman_words.word_list)
print(logo)

lives = 6

display = []
for letter in chosen_word:
    display += "_"
print(display)

end_of_game = False

while not end_of_game:
    #todo - 2 Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
    guess = input("Guess the letter: ").lower()
    
    #todo - 3 Check if the letter the user guessed is one of the letters in the chosen_word.
    if guess in display:
        print(f"You've already guessed{guess}")
    
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        print(f"You've guessed{guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
    
    print(f"{' '.join(display)}")
    
    if "_" not in display:
        end_of_game = True
        print("Hurray! You win.")    
    
    print(stages[lives])
    