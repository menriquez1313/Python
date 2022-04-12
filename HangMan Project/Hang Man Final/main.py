#Step 5

import random
from hangman_art import logo, stages #Logo and Stages are imported from hangman_art
from hangman_words import word_list #New word list is imported from hangman_words file

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
letters_used = []
for _ in range(word_length):
    display += "_"

print(logo) # LOGO Print!

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    
    if guess in display:
      print(f"Letter {guess} has been guessed already. Choose another letter.")
        
    #Check guessed letter
    for position in range(word_length):
      letters_used.append(guess) #add letter if it hasn't been guessed twice.
      letter = chosen_word[position]
      #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
      if letter == guess:
          display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
      #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
      lives -= 1
      print(f"The letter {guess} is not in the word.")
      if lives == 0:
        end_of_game = True
        print("YOU LOSE!")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("YOU WIN!")

    print(stages[lives])