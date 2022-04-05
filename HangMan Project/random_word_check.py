#Step 1 
import random

rand_number = int(random.random()*2) #random number generator
word_list = ["aardvark", "baboon", "camel"]
#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

word = word_list[rand_number]


#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

letter = input("Guess a random letter! (lower case) ")

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
print(word)

for word_letter in word:
  
  if word_letter == letter:
    print("True")
  else:
    print("False")
