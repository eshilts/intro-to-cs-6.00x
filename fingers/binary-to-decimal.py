binary_number = raw_input("Enter a binary number: ")

total = 0

for i, digit in enumerate(binary_number[::-1]):
  if int(digit) not in [0, 1]:
    raise "Not a binary number!"
  total += (2 ** i) * int(digit)

print "Binary = {0}, Decimal = {1}".format(binary_number, total)

