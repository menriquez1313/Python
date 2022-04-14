from replit import clear
from art import logo

bidders = {
}

#adds names to the bidder dictionary.
def add_bidders(bidders_name, bidders_bid):
  bidders[bidders_name] = bidders_bid

#checks the winner within the bidders dictionary. 
def check_winner():
  highest_bid = 0
  for check in bidders:
    check_bid = int(bidders[check])
    if check_bid > highest_bid:
      highest_bid = check_bid
  print(f"The winner is {check} with a bid of ${highest_bid}!\n")
    
#HINT: You can call clear() to clear the output in the console.

print(logo)
any_bidders = True

#User enters Name, bid, and loops if user wants more bidders.
while any_bidders == True:
  name = input("What is your name? ")
  bid = input("What's your bid? $")
  more_bids = input("Are there any other bidders? Type 'yes' or 'no' ")
  
  add_bidders(name, bid) #calls add_bidders to add bidders in Dictionary.

  if more_bids == "no":
    any_bidders = False
    clear()
  else:
    clear()
    
check_winner() #calls winner definition if user inputs NO
