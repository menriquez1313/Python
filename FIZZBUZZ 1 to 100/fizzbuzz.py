#Write your code below this row 👇

for number in range (1,101):
  #print(number)
  if (number % 5 == 0) and (number % 3 == 0):
      print("FIZZBUZZ")
  elif (number % 5 == 0):
    print("BUZZ")
  elif(number % 3 == 0):
    print("FIZZ")
  else:
    print(number)