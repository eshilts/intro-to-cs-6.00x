def odd(num):
  return num % 2 == 1

found_an_odd = False

print("Get ready to enter 10 integers.")

for i in range(10):
  latest = int(raw_input("Integer [{0}]: ".format(i + 1)))

  if odd(latest):
    if found_an_odd:
      highest = max(latest, highest)
    else:
      highest = latest
      found_an_odd = True

if found_an_odd:
  print "Highest odd = ", highest
else:
  print "No odds found"
