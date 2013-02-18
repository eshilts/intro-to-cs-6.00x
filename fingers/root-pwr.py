x = int(raw_input('Enter an integer: '))

ans = 0
root = 0

while root < abs(x):
  for pwr in range(7):
    if root**pwr == x:
      print "Root = ", root, " - Power = ", pwr
      ans = root
  root += 1

if ans == 0:
  print "Answer does not exist"
