alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  finished_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char in alphabet:
      shift_num = alphabet.index(char) + shift_amount
      new_letter = alphabet[shift_num]
      finished_text += new_letter
    else: #keeps anything not in the alphabet unchanged in the string (spaces, numbers, symbols)
      finished_text += char
    
  print(f"Here's the {cipher_direction}d result: {finished_text}")

from art import logo

print(logo) 

ask_user = True #keeps while loop going until user does not want to repeat. 
while ask_user == True:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  
  shift = shift % 26 #if any number goes over 26
  
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
  
  question = input("Do you want to restart? Y or N:\n").lower()
  if question == "n":
    ask_user = False