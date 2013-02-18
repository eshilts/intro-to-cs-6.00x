print "Please think of a number between 0 and 100!"

low = 0
high = 100
guess = (high + low) / 2

while True:
  print "Is your secret number ", guess, "?"
  feedback = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")

  if feedback == 'l':
    low = guess
  elif feedback == 'h':
    high = guess
  elif feedback == 'c':
    break
  else:
    print "Sorry, I did not understand your input."
    next

  guess = (high + low) / 2

print "Game over. Your secret number was: ", guess
