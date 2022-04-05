rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random

x = input("Choose rock, paper, or scissors? \n")
r = random.randint(0, 2)

rps = ["rock", "paper", "scissors"]

if x == "rock":
  if rps[r] == "rock":
    print("You: ")
    print(rock)
    print("Computer: ")
    print(rock)
    print("Tie!")
  elif rps[r] == "paper":
    print("You: ")
    print(rock)
    print("Computer: ")
    print(paper)
    print("Lose!")
  else:
    print("You: ")
    print(rock)
    print("Computer: ")
    print(scissors)
    print("Win!")
    
elif x == "paper":
  if rps[r] == "rock":
    print("You: ")
    print(paper)
    print("Computer: ")
    print(rock)
    print("Win!")
  elif rps[r] == "paper":
    print("You: ")
    print(paper)
    print("Computer: ")
    print(paper)
    print("Tie!")
  else:
    print("You: ")
    print(paper)
    print("Computer: ")
    print(scissors)
    print("Lose!")

else:
  if rps[r] == "rock":
    print("You: ")
    print(scissors)
    print("Computer: ")
    print(rock)
    print("Lose!")
  elif rps[r] == "paper":
    print("You: ")
    print(scissors)
    print("Computer: ")
    print(paper)
    print("Win!")
  else:
    print("You: ")
    print(scissors)
    print("Computer: ")
    print(scissors)
    print("Tie!")