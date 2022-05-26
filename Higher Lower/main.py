"""This is the HIGHER LOWER Game. 
Two different informations will be compared and the user will have to
guess which one among the two are the most popular. For each correct answer will get a point.
GOOD LUCK AND HAVE FUN! """

from art import logo
from art import vs
from game_data import data
import random
import replit

#Get's information from game_data.py
def get_info():
  pick = random.choice(data)
  name = pick.get("name")
  count = int(pick.get("follower_count"))
  desc = pick.get("description")
  country = pick.get("country")
  print(f"{name}, a {desc}, from {country}.")
  return count

  #Checks for the right or wrong answer
def print_info():

  print("Compare:")
  a = get_info()
  print(vs)
  print("Against:")
  b = get_info()

  if input("Who has more followers 'A' or 'B': ") == a:
    if a > b:
      replit.clear()
      print("Correct! +1 point!")
      return True
  
    else:
      replit.clear()
      print("Wrong! Sorry. :(")
      return False
  else:
    if b > a:
      replit.clear()
      print("Correct! +1 point!")
      return True 
      
    else:
      replit.clear()
      print("Wrong! Sorry. :(")
      return False
      
print(logo)

game_on = True
points = 0
how_many_tries = 0

while game_on == True: #Repeat game until false.
  how_many_tries += 1 

  #checks the returns for TRUE or FALSE
  #Scores are than added for each TRUE answer
  if print_info() == True: 
    points += 1
    print(f"Score: {points}")
    
  else:
    print(f"Score: {points}")

  #Checks how many times the game is played.
  #After game is finished, the FINAL SCORE is outputted. 
  if how_many_tries == 10: 
    replit.clear()
    print(f"Final Score: {points}! ")
    game_on = False
  