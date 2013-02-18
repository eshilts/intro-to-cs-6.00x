x = int(raw_input("Enter an integer to find the cube root of: "))

if x < 0:
  negative = True
  x = -x
else:
  negative = False

epsilon = 0.01
numGuesses = 0
low = 0.0
high = max(1.0, x)
ans = (high + low) / 2.0

while abs(ans ** 3 - x) >= epsilon:
  print "low = {0}, high = {1}, ans = {2}".format(low, high, ans)
  numGuesses += 1
  if numGuesses > 50:
    break

  if ans ** 3 < x:
    low = ans
  else:
    high = ans
  ans = (high + low) / 2.0

if negative:
  ans = -ans

print "numGuesses = ", numGuesses
print ans, " is close to the cube root of ", x
