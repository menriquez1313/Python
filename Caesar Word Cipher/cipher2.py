alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amount):
  cipher_text = ""
  for i in plain_text:
    #print(alphabet.index(i))
    shift_num = shift_amount + alphabet.index(i)
    if shift_num > 25:
      shift_num -= 26
    new_letter = alphabet[shift_num]
    cipher_text += new_letter
  print(cipher_text)

def decrypt(crypt_text, shift_amount):
  decipher_text = ""
  for i in crypt_text:
    shift_num = alphabet.index(i) - shift_amount
    if shift_num < 0:
        shift_num += 26
    new_letter = alphabet[shift_num]
    decipher_text += new_letter
  print(decipher_text)
  
#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
#decrypt(text, shift)
  #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
  #e.g. 
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"


#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
if direction == "encode":
  encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
  decrypt(crypt_text=text, shift_amount=shift)
