def odd(num):
  return num % 2 == 1

def largest_odd(x, y , z):
  if not (odd(x) or odd(y) or odd(z)):
    print "No odd numbers"
  else:
    if odd(x) and odd(y) and odd(z):
      print max(x, y, z)
    elif odd(x) and odd(y):
      print max(x, y)
    elif odd(x) and odd(z):
      print max(x, z)
    elif odd(y) and odd(z):
      print max(y, z)
    elif odd(x):
      print x
    elif odd(y):
      print y
    else:
      print z

largest_odd(1, 2, 3)
largest_odd(0, 2, 4)
largest_odd(11, 9, 7)
